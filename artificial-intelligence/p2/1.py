import random
import math 
from functools import lru_cache

random.seed(42)

def opt_dist(lst, d):
    return cached_opt_dist(tuple(lst), tuple(d))

#lru cache dalo duzo

@lru_cache(maxsize=None) 
def cached_opt_dist(lst_tuple, d_tuple):
    lst = list(lst_tuple)
    d = list(d_tuple)
    n = len(lst)

    if not d:
        return sum(lst)
    
    best = float('inf')

    def place_run(index, pos, candidate):
        nonlocal best
        if index == len(d):
            # gdy index == len(d), rozmiescilismy wszystkie bloki ze spec, pozostale uzupelniamy zerami, i porownujemy z best
            candidate_ext = candidate + [0] * (n - len(candidate))
            cost = sum(1 for a,b in zip(candidate_ext, lst) if a != b)
            best = min(best, cost)
            return
        # ustalamy dlugosc bloku ktoremy chcemy rozmiescic
        run_len = d[index]
        min_space_after = 0
        for r in d[index + 1 : ]:
            min_space_after = min_space_after + r + 1
        # minspaceafter to minimalna przestrzen dla pozostalych blokow
        # mozliwe pozycje startowe dla bloku ktory chcemy rozmiescic tzn run_len, tak aby pzoostala przestrzen dla pozostalcyh blokow
        # rekurencyjnie wywolujey 
        for start in range(pos, n - run_len - min_space_after + 1):
            new_candidate = candidate + [0] * (start - len(candidate)) + [1] * run_len
            next_pos = start + run_len + 1
            place_run(index + 1, next_pos, new_candidate)
    place_run(0, 0, [])
    return best

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

def all_combs(row_length, spec):
    results = []
    if not spec:
        return [[0] * row_length]
    def aux(index, pos, current):
        if index == len(spec):
            if pos <= row_length:
                candidate = current + [0] * (row_length - pos)
                results.append(candidate)
            return
        run = spec[index]

        min_required = sum(spec[i] for i in range(index, len(spec))) + (len(spec) - index - 1)

        for start in range(pos, row_length - min_required + 1):
            candidate = current + [0] * (start - pos) + [1] * run
            new_pos = start + run            
            if index < len(spec) - 1:
                candidate.append(0)
                new_pos += 1
            aux(index + 1, new_pos, candidate)
    aux(0, 0, [])
    return results

def intersection_lists(lists):
    if not lists:
        return []
    return [1 if all(x == 1 for x in group) else 0 for group in zip(*lists)]

def solver(spec, length):
    allcombs = all_combs(length, spec)
    return intersection_lists(allcombs)



def main(row_spec, col_spec, iters=2000000):
    X = len(row_spec)
    Y = len(col_spec)
    orig_grid = [
        [ 0 for _ in range(Y) ] for _ in range(X)
    ]

    for i in range(X):
        orig_grid[i] = solver(row_spec[i], Y)

    for i in range(Y):
        new_col = solver(col_spec[i], X)
        for j in range(len(new_col)):
            if orig_grid[j][i] == 0 and new_col[j] == 1:
                orig_grid[j][i] = 1

    grid = [ row[:] for row in orig_grid ]

    row_todo = get_bad_rows(grid, row_spec)
    col_todo = get_bad_columns(grid, col_spec)

    cooling_rate=0.99999
    temperature = 0.05
    
    while True:
        # jesli nie ma zlych kolumn i wierszy to ok
        if not row_todo and not col_todo:
            return grid
        
        # temperature *= cooling_rate

        # if random.random() < temperature:
        #     possible_cols = [c for c in range(Y) if orig_grid[r][c] != 1]
        #     possible_rows = [r for r in range(X) if orig_grid[r][c] != 1]
        #     if possible_cols == [] or possible_rows == []:
        #         continue
        #     r_rand = random.choice(possible_rows)
        #     c_rand = random.choice(possible_cols)
        #     grid[r_rand][c_rand] = 1 - grid[r_rand][c_rand]

        #     row_todo = get_bad_rows(grid, row_spec)
        #     col_todo = get_bad_columns(grid, col_spec)
        #     continue
            


                
        
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
                if orig_grid[r][c] == 1:
                    continue
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
                possible_indices = [c for c in range(Y) if orig_grid[r][c] != 1]
                if possible_indices == []:
                    continue
                c_rand = random.choice(possible_indices)

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
                if orig_grid[r][c] == 1:
                    continue
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
                possible_indices = [r for r in range(X) if orig_grid[r][c] != 1]
                if possible_indices == []:
                    continue
                r_rand = random.choice(possible_indices)
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




with open("zad_input.txt", encoding="utf-8") as fin, \
     open("zad_output.txt", "w", encoding="utf-8") as fout:
    input_arr = []
    for line in fin:
        input_arr.append(line.strip())
    spec = input_arr[0].split(" ")
    desc = input_arr[1:]
    rozmiar_X_obrazka, rozmiar_Y_obrazka = int(spec[0]), int(spec[1])
    row_spec = []
    col_spec = []
    for i in range(rozmiar_X_obrazka):
        d = desc[i].split(" ")
        for i in range(len(d)):
            d[i] = int(d[i])
        row_spec.append(d)
    for i in range(rozmiar_Y_obrazka):
        d = desc[rozmiar_X_obrazka + i].split(" ")
        for i in range(len(d)):
            d[i] = int(d[i])
        col_spec.append(d)
    e = main(row_spec, col_spec)

    for wiersz in e:
        strwiersz = ''
        for number in wiersz:
            if number == 1:
                strwiersz += '#'
            else:
                strwiersz += '.'
        fout.write(strwiersz + '\n')