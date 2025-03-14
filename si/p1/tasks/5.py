# idea rozwiazania: tak jak podano w zadaniu; uzyjemy funkcji z zadania 4 aby liczyc czy pokolorowanie danego pola/odkolorwanie zmieni nam dystans do poprawnego kolorowania (ile pol trzeba jeszcze zmienic). z tych dla ktorych jest najlepsza poprawa wybieramy losowo, jesli nie ma poprawy to losowo totalnie,w zadaniu bylo ze z malym prawdopodobienstwem robimy jakis wybor nieoptymalnie, ale nie implemnetujac tego tez dziala

import random

def opt_dist(lst, d):
    n = len(lst)
    min_changes = float('inf')            
    for start in range(0, n - d + 1):
        changes = 0        
        for i in range(start, start + d):
            if lst[i] == 0:
                changes += 1        
        for i in range(0, start):
            if lst[i] == 1:
                changes += 1
        for i in range(start + d, n):
            if lst[i] == 1:
                changes += 1
        
        if changes < min_changes:
            min_changes = changes
    
    return min_changes

def row_distance(row, d):
    if d == 0:
        return sum(row)
    else:
        return opt_dist(row, d)

def col_distance(grid, col_idx, d):
    col = [grid[r][col_idx] for r in range(len(grid))]
    if d == 0:
        return sum(col)
    else:
        return opt_dist(col, d)

def get_bad_rows(grid, row_spec):
    bads = []
    for r in range(len(grid)):
        dist = row_distance(grid[r], row_spec[r])
        if dist > 0:
            bads.append(r)
    return bads

def get_bad_columns(grid, col_spec):
    bads = []    
    Y = len(col_spec)   # liczba kolumn
    for c in range(Y):
        dist = col_distance(grid, c, col_spec[c])
        if dist > 0:
            bads.append(c)
    return bads


def score(grid, row_spec, col_spec):
    s = 0
    for r in range(len(grid)):
        s += row_distance(grid[r], row_spec[r])
    for c in range(len(col_spec)):
        s += col_distance(grid, c, col_spec[c])
    return s



def main(row_spec, col_spec, iters=100000):
    X = len(row_spec)
    Y = len(col_spec)
    grid = [
        [ random.choice([0, 1]) for _ in range(Y) ] for _ in range(X)
    ]

    row_todo = get_bad_rows(grid, row_spec)
    col_todo = get_bad_columns(grid, col_spec)
    
    for i in range(iters):
        # jesli nie ma zlych kolumn i wierszy to ok
        if not row_todo and not col_todo:
            return grid
        
        # wybieramy co poprawiqamy        
        if row_todo and col_todo:
            choice = random.choice(["row", "col"])
        elif row_todo:
            choice = "row"
        else:
            choice = "col"

        if choice == 'row':
            r = random.choice(row_todo)
            old_rdist = row_distance(grid[r], row_spec[r])

            best_improvement = 0
            best_positions = []

            # Sprawdzamy każdy piksel w tym wierszu
            for c in range(Y):
                # Bieżący błąd kolumny c:
                old_cdist = col_distance(grid, c, col_spec[c])

                # Symulujemy flip:
                grid[r][c] = 1 - grid[r][c]

                new_rdist = row_distance(grid[r], row_spec[r])
                new_cdist = col_distance(grid, c, col_spec[c])

                # Różnica = (old_rdist + old_cdist) - (new_rdist + new_cdist)
                improvement = (old_rdist + old_cdist) - (new_rdist + new_cdist)

                # Cofamy flip
                grid[r][c] = 1 - grid[r][c]

                if improvement > best_improvement:
                    best_improvement = improvement
                    best_positions = [(r, c)]
                elif improvement == best_improvement and improvement > 0:
                    best_positions.append((r, c))
            
            # Jeżeli mamy jakąś poprawę, to losowo wybierzmy jedną pozycję z best_positions
            if best_improvement > 0:
                (r2, c2) = random.choice(best_positions)
                # Wykonujemy flip
                grid[r2][c2] = 1 - grid[r2][c2]
                # Aktualizujemy row_todo, col_todo
                #  - sprawdź, czy wiersz r2 nadal jest zły
                if row_distance(grid[r2], row_spec[r2]) == 0:
                    if r2 in row_todo:
                        row_todo.remove(r2)
                else:
                    if r2 not in row_todo:
                        row_todo.append(r2)

                #  - sprawdź, czy kolumna c2 nadal jest zła
                if col_distance(grid, c2, col_spec[c2]) == 0:
                    if c2 in col_todo:
                        col_todo.remove(c2)
                else:
                    if c2 not in col_todo:
                        col_todo.append(c2)
            else:
                # Jeśli brak poprawy – można np. wykonać losowy flip
                # albo nic nie robić. Wstawiamy "losowy flip" jako tie-break:
                c_rand = random.randint(0, Y-1)
                grid[r][c_rand] = 1 - grid[r][c_rand]
                # aktualizacja row_todo, col_todo:
                if row_distance(grid[r], row_spec[r]) == 0:
                    if r in row_todo:
                        row_todo.remove(r)
                else:
                    if r not in row_todo:
                        row_todo.append(r)
                if col_distance(grid, c_rand, col_spec[c_rand]) == 0:
                    if c_rand in col_todo:
                        col_todo.remove(c_rand)
                else:
                    if c_rand not in col_todo:
                        col_todo.append(c_rand)
        else:            
            c = random.choice(col_todo)
            old_cdist = col_distance(grid, c, col_spec[c])

            best_improvement = 0
            best_positions = []

            for r in range(X):
                old_rdist = row_distance(grid[r], row_spec[r])

                # flip
                grid[r][c] = 1 - grid[r][c]
                new_rdist = row_distance(grid[r], row_spec[r])
                new_cdist = col_distance(grid, c, col_spec[c])
                improvement = (old_rdist + old_cdist) - (new_rdist + new_cdist)

                # cofnij
                grid[r][c] = 1 - grid[r][c]

                if improvement > best_improvement:
                    best_improvement = improvement
                    best_positions = [(r, c)]
                elif improvement == best_improvement and improvement > 0:
                    best_positions.append((r, c))
            
            if best_improvement > 0:
                (r2, c2) = random.choice(best_positions)
                # flip
                grid[r2][c2] = 1 - grid[r2][c2]
                # aktualizacja row_todo, col_todo
                if row_distance(grid[r2], row_spec[r2]) == 0:
                    if r2 in row_todo:
                        row_todo.remove(r2)
                else:
                    if r2 not in row_todo:
                        row_todo.append(r2)

                if col_distance(grid, c2, col_spec[c2]) == 0:
                    if c2 in col_todo:
                        col_todo.remove(c2)
                else:
                    if c2 not in col_todo:
                        col_todo.append(c2)
            else:
                # brak poprawy => losowy flip
                r_rand = random.randint(0, X-1)
                grid[r_rand][c] = 1 - grid[r_rand][c]
                # aktualizacja
                if row_distance(grid[r_rand], row_spec[r_rand]) == 0:
                    if r_rand in row_todo:
                        row_todo.remove(r_rand)
                else:
                    if r_rand not in row_todo:
                        row_todo.append(r_rand)
                if col_distance(grid, c, col_spec[c]) == 0:
                    if c in col_todo:
                        col_todo.remove(c)
                else:
                    if c not in col_todo:
                        col_todo.append(c)            

    return 'not found'




with open("zad5_input.txt", encoding="utf-8") as fin, \
     open("zad5_output.txt", "w", encoding="utf-8") as fout:
    input_arr = []
    for line in fin:
        input_arr.append(line.strip())
    spec = input_arr[0].split(" ")
    desc = input_arr[1:]
    rozmiar_X_obrazka, rozmiar_Y_obrazka = int(spec[0]), int(spec[1])
    row_spec = []
    col_spec = []
    for i in range(rozmiar_X_obrazka):
        row_spec.append(int(desc[i]))
    for i in range(rozmiar_Y_obrazka):
        col_spec.append(int(desc[rozmiar_X_obrazka + i]))
    e = main(row_spec, col_spec)

    for wiersz in e:
        strwiersz = ''
        for number in wiersz:
            if number == 1:
                strwiersz += '#'
            else:
                strwiersz += '.'
        fout.write(strwiersz + '\n')




    


# jakich funkcji potrzebujemy?
# sprawdzajacych czy obrazek jest OK
# sprawdzajacych czy wiersz/kolumna jest ok







