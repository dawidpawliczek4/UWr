import collections

def pos_to_coord(pos):
    """Przekształca pozycję w notacji szachowej (np. 'c4') na współrzędne (wiersz, kolumna)."""
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return (row, col)

def in_bounds(r, c):
    """Sprawdza, czy współrzędne mieszczą się w granicach planszy 8x8."""
    return 0 <= r < 8 and 0 <= c < 8

def kings_adjacent(pos1, pos2):
    """Sprawdza, czy dwa pola (pozycje królów) sąsiadują ze sobą (w tym diagonalnie)."""
    return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1

def rook_attacks_square(rook, square, wk):
    """
    Sprawdza, czy wieża na pozycji 'rook' atakuje pole 'square'.
    Jeśli między wieżą a celem stoi biały król (wk), to atak jest zablokowany.
    """
    # Sprawdzenie ataku w poziomie:
    if rook[0] == square[0]:
        r = rook[0]
        c1, c2 = sorted([rook[1], square[1]])
        if wk[0] == r and c1 < wk[1] < c2:
            return False
        return True
    # Sprawdzenie ataku w pionie:
    if rook[1] == square[1]:
        c = rook[1]
        r1, r2 = sorted([rook[0], square[0]])
        if wk[1] == c and r1 < wk[0] < r2:
            return False
        return True
    return False

def is_black_in_check(state):
    """
    Dla danego stanu (turn, wk, wr, bk) sprawdza, czy czarny król (bk)
    jest atakowany przez białą wieżę.
    """
    _, wk, wr, bk = state
    return rook_attacks_square(wr, bk, wk)

def generate_white_moves(state):
    """
    Generuje wszystkie legalne stany powstałe z ruchu białych.
    Białe mogą przesunąć:
      - króla: o jedno pole we wszystkich kierunkach (z zachowaniem ograniczeń, m.in.
        nie mogą wejść na pole zajęte lub sąsiadujące z czarnym królem),
      - wieżę: poruszając się w pionie lub poziomie, nie przeskakując przez figury.
    Po wykonaniu ruchu następuje zmiana strony (turn -> "black").
    """
    turn, wk, wr, bk = state
    next_states = []

    # Ruchy białego króla
    king_dirs = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]
    for dr, dc in king_dirs:
        new_wk = (wk[0] + dr, wk[1] + dc)
        if not in_bounds(new_wk[0], new_wk[1]):
            continue
        # Nie można wejść na pole zajęte przez wieżę lub czarnego króla
        if new_wk == wr or new_wk == bk:
            continue
        # Króle nie mogą być na sąsiednich polach
        if kings_adjacent(new_wk, bk):
            continue
        next_states.append(("black", new_wk, wr, bk))

    # Ruchy białej wieży
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in rook_dirs:
        steps = 1
        while True:
            new_wr = (wr[0] + dr * steps, wr[1] + dc * steps)
            if not in_bounds(new_wr[0], new_wr[1]):
                break
            # Wieża nie może wejść na pole zajęte przez białego króla ani czarnego króla
            if new_wr == wk or new_wr == bk:
                break
            next_states.append(("black", wk, new_wr, bk))
            steps += 1

    return next_states

def generate_black_moves(state):
    """
    Generuje wszystkie legalne stany powstałe z ruchu czarnego króla.
    Czarny król może przesunąć się o jedno pole we wszystkich kierunkach,
    ale nie może wejść na pole zajęte przez białe figury, wejść na pole atakowane
    przez wieżę (chyba, że droga jest zablokowana przez białego króla) lub sąsiadować z białym królem.
    Po wykonaniu ruchu następuje zmiana strony (turn -> "white").
    """
    turn, wk, wr, bk = state
    next_states = []
    king_dirs = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]
    for dr, dc in king_dirs:
        new_bk = (bk[0] + dr, bk[1] + dc)
        if not in_bounds(new_bk[0], new_bk[1]):
            continue
        # Czarny król nie może wejść na pole zajęte przez białe figury
        if new_bk == wk or new_bk == wr:
            continue
        # Króle nie mogą być na sąsiednich polach
        if kings_adjacent(new_bk, wk):
            continue
        # Czarny król nie może przejść na pole atakowane przez wieżę (jeśli nie jest zablokowane przez białego króla)
        if rook_attacks_square(wr, new_bk, wk):
            continue
        next_states.append(("white", wk, wr, new_bk))
    return next_states

def is_checkmate(state):
    """
    Sprawdza, czy dany stan jest matowy:
      - Ruch należy do czarnych,
      - Czarny król jest szachowany (przez wieżę),
      - Czarny król nie ma żadnych legalnych ruchów.
    """
    turn, wk, wr, bk = state
    if turn != "black":
        return False
    if not is_black_in_check(state):
        return False
    # Jeśli czarny król nie ma żadnego legalnego ruchu, to jest mat.
    return len(generate_black_moves(state)) == 0

def bfs(initial_state):
    """
    Przeszukiwanie wszerz (BFS) przestrzeni stanów.
    Zwraca minimalną liczbę ruchów prowadzącą do mata lub -1, gdyby nie dało się osiągnąć mata.
    """
    queue = collections.deque()
    queue.append((initial_state, 0))
    visited = set()
    visited.add(initial_state)
    
    while queue:
        state, moves = queue.popleft()
        if is_checkmate(state):
            return moves
        turn = state[0]
        if turn == "white":
            next_states = generate_white_moves(state)
        else:
            next_states = generate_black_moves(state)
        for ns in next_states:
            if ns not in visited:
                visited.add(ns)
                queue.append((ns, moves + 1))
    return -1

def parse_input_line(line):
    """
    Przetwarza linię wejścia w formacie:
      "kolor bialy_król biała_wieza czarny_król"
    np. "black c4 c8 h3".
    Zwraca stan w postaci: (turn, wk, wr, bk)
    """
    parts = line.split()
    turn = parts[0]
    wk = pos_to_coord(parts[1])
    wr = pos_to_coord(parts[2])
    bk = pos_to_coord(parts[3])
    return (turn, wk, wr, bk)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python zad1.py zad1_input.txt")
        return
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            state = parse_input_line(line)
            moves = bfs(state)
            print(moves)

if __name__ == "__main__":
    main()
