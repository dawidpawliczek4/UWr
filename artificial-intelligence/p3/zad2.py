import random
import math 
from functools import lru_cache
import copy

random.seed(43)


@lru_cache(maxsize=None)
def all_combs_cache(row_length, spec_tuple):
    spec = list(spec_tuple)
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

def all_combs(row_length, spec):
    return all_combs_cache(row_length, tuple(spec))

def intersection_lists(lists):
    if not lists:
        return []
    return [1 if all(x == 1 for x in group) else 0 if all(x == 0 for x in group) else -1 for group in zip(*lists)]

def solver(spec, length, actual_row):
    allcombs = all_combs(length, spec)

    def filterFun(lst):
        for i in range(len(lst)):
            if (actual_row[i] == 1 or actual_row[i] == 0 )and lst[i] != actual_row[i]:
                return False
        return True
    
    allcombsfiltered = list(filter(filterFun, allcombs))
    
    rets =  intersection_lists(allcombsfiltered)
    
    return rets

def is_ready_grid(grid):
    for row in grid:
        if -1 in row:
            return False
    return True

@lru_cache(maxsize=None)
def random_position_cache(grid):
    grid = [list(row ) for row in grid]
    rows_todo = [row.count(-1) for row in grid]
    rows_todo_positivie = [ row for row in rows_todo if row > 0 ]
    min_row = min(rows_todo_positivie)
    i = rows_todo.index(min_row)
    min_row = grid[i]


    positions = [ (i, j) for j, v in enumerate(min_row) if v == -1]
    

    # positions = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == -1]
    return random.choice(positions)


def random_position(grid):
    return random_position_cache(tuple(tuple(row) for row in grid))


def propagate(grid, row_spec, col_spec, X, Y):    
    changes = True
    while changes:
        changes = False
        for i in range(X):
            new_row = solver(row_spec[i], Y, grid[i])
            if len(new_row) == 0:
                return None
            for j in range(Y):
                if grid[i][j] == -1 and new_row[j] != -1:
                    grid[i][j] = new_row[j]
                    changes = True

        for col_idx in range(Y):
            col = [grid[r][col_idx] for r in range(len(grid))]
            new_col = solver(col_spec[col_idx], X, col)

            if len(new_col) == 0:
                return None

            for j in range(len(new_col)):
                if grid[j][col_idx] == -1 and new_col[j] != -1:
                    grid[j][col_idx] = new_col[j]
                    changes = True

    return is_ready_grid(grid)


def backtrack(grid, row_spec, col_spec, X, Y):
    res = propagate(grid, row_spec, col_spec, X, Y)
    if res is None:
        return None
    if res is True:
        return grid
    
    
    i, j = random_position(grid)

    for guess in [0, 1]:
        new_grid = copy.deepcopy(grid)
        new_grid[i][j] = guess

        sol = backtrack(new_grid, row_spec, col_spec, X, Y)
        if sol is not None:
            return sol
    return None


def main(row_spec, col_spec, max_reps = 1000):
    X = len(row_spec)
    Y = len(col_spec)
    grid = [
        [ -1 for _ in range(Y) ] for _ in range(X)
    ]
    
    return backtrack(grid, row_spec, col_spec, X, Y)


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