# uzyjemy bfsa, dla kazdej iteracji generujemy wszystkie mozliwe poprawne ruchy 'generate_moves(state)', jesli tego stanu jeszcze nie bylo to rozwazamy

import collections

def reconstruct_path(final_state, parent):
    """
    Cofamy się po słowniku parent od final_state do stanu początkowego.
    Zwracamy listę opisów ruchów w kolejności od pierwszego do ostatniego.
    """    
    moves = [final_state]
    current = final_state
    
    while True:
        prev_state = parent[current]
        if prev_state is None:
            # Dotarliśmy do stanu początkowego
            break
        # move_desc to opis ruchu, który doprowadził z prev_state do current
        moves.append(prev_state)
        current = prev_state

    moves.reverse()
    return moves

def bfs(initial_state, debug=False):
    queue = collections.deque([(initial_state, 0)])  # stan + liczba ruchów
    visited = set([initial_state])
    parent = {initial_state: None}
    
    while queue:
        state, moves = queue.popleft()
        if is_checkmate(state):
            if debug:
                return (moves, reconstruct_path(state, parent))                
            return moves
        for next_state in generate_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state
                queue.append((next_state, moves + 1))
    return "INF"

def is_checkmate(state: tuple):        
    if state[0] == 'white':
        return False
    if not is_black_in_check(state):
        return False
    return len(generate_black_moves(state)) == 0    
    

def generate_moves(state):
    if state[0] == 'white':
        return generate_white_moves(state) 
    return generate_black_moves(state)
    
def is_black_in_check(state):
    turn, wk, wr, bk = state
    return rook_attacks_square(wr, bk, wk)

def kings_adj(bk, wk):
    return abs(bk[0] - wk[0]) <= 1 and abs(bk[1] - wk[1]) <= 1

def rook_attacks_square(rook, square, wk):
    if rook[0] == square[0]:
        c1, c2 = sorted([rook[1], square[1]])
        if wk[0] == rook[0] and c1 < wk[1] < c2:
            return False
        return True
    
    if rook[1] == square[1]:
        c1, c2 = sorted([rook[0], square[0]])
        if wk[1] == rook[1] and c1 < wk[0] < c2:
            return False
        return True
    
    return False
    

def is_bounds(r, c):
    return 0 <= r <= 7 and 0 <= c <= 7

def generate_black_moves(state):    
    turn, wk, wr, bk = state
    possible_king_moves = [ (-1, 1), (0, 1), (1, 1),
                            (-1, 0),         (1, 0),
                            (-1, -1), (0, -1), (1, -1)                            
                           ]
    next_states = []

    for move in possible_king_moves:
        new_king_state = (bk[0] + move[0], bk[1] + move[1])    
        if not is_bounds(new_king_state[0], new_king_state[1]):
            continue
        if new_king_state == bk or new_king_state == wk:
            continue
        if kings_adj(new_king_state, wk):
            continue
        if rook_attacks_square(wr, new_king_state, wk):
            continue
        next_state = ("white", wk, wr, new_king_state)
        next_states.append(next_state)
    return next_states

def generate_white_moves(state):
    turn, wk, wr, bk = state
    possible_king_moves = [ (-1, 1), (0, 1), (1, 1),
                        (-1, 0),         (1, 0),
                        (-1, -1), (0, -1), (1, -1)                            
                        ]
    next_states = []
    for move in possible_king_moves:
        new_king_state = (wk[0] + move[0], wk[1] + move[1])    

        if not is_bounds(new_king_state[0], new_king_state[1]):
            continue
        if new_king_state == wr or new_king_state == bk:
            continue
        if kings_adj(new_king_state, bk):
            continue
        next_state = ("black", new_king_state, wr, bk)
        next_states.append(next_state)
    
    possible_rock_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in possible_rock_moves:
        steps = 1
        while True:
            new_wr = (wr[0] + move[0] * steps, wr[1] + move[1] * steps)
            if not is_bounds(new_wr[0], new_wr[1]):
                break
            if new_wr == wk or new_wr == bk or new_wr == wr:
                break
            if not kings_adj(new_wr, bk):                
                next_state = ("black", wk, new_wr, bk)
                next_states.append(next_state)
            steps += 1

    return next_states


def to_number_state(s):
    return (ord(s[0]) - ord('a'), int(s[1]) - 1)

with open("zad1_input.txt", encoding="utf-8") as fin, \
     open("zad1_output.txt", "w", encoding="utf-8") as fout:
    for line in fin:        
        t = line.strip().split(" ")
        t[1] = to_number_state(t[1])
        t[2] = to_number_state(t[2])
        t[3] = to_number_state(t[3])
        
        out = bfs((t[0], t[1], t[2], t[3]), True)        
        fout.write(str(out) + "\n")                  
