import collections
import heapq

def do_move(spec, state, move):
    new_state = []
    for x, y in state:
        if move == 'U' and spec[x - 1][y] != '#':
            new_state.append((x - 1, y))
        elif move == 'D' and spec[x + 1][y] != '#':
            new_state.append((x + 1, y))
        elif move == 'L' and spec[x][y - 1] != '#':
            new_state.append((x, y - 1))
        elif move == 'R' and spec[x][y + 1] != '#':
            new_state.append((x, y + 1))
        else:
            new_state.append((x, y))
    return new_state


def generate_moves(spec, state, path):
    all_new_states = []
    for move in ['U', 'D', 'L', 'R']:
        all_new_states.append((do_move(spec, state, move), path + move))
    return all_new_states

def heuristic_fn(state, goals):
    return min(abs(x1 - x2) + abs(y1 - y2) for (x2, y2) in goals for x1, y1 in state)

def lower_uncertanity(spec, state):
    tuple_start = tuple(set(state))
    queue = collections.deque([(tuple_start, '')])
    visited = {tuple_start}
    lowest = float('inf')
    while queue:
        pos, path_to_state = queue.popleft()
        if len(pos) > lowest:
            continue
        else:
            lowest = len(pos)
        new_states = generate_moves(spec, pos, path_to_state)
        for new_state, new_path in new_states:
            tuple_new = tuple(set(new_state))
            if len(tuple_new) <= 3:
                return (tuple_new, new_path)
            if tuple_new in visited:
                continue
            visited.add(tuple_new)
            queue.append((tuple_new, new_path))


def astar(spec, state, goals, h):
    state, path = state
    state = tuple(set(state))
    prioque = []    
    # w heapq umieszcamy (f(n), g(n), state, path)
    heapq.heappush(prioque, (h(state, goals), 0, state, path))
    visited = {state}
    
    while prioque:
        f, g, state, path = heapq.heappop(prioque)               

        if all(pozycja in goals for pozycja in state):
            return path
        
        four_new_states = generate_moves(spec, state, path)
        for new_state in four_new_states:
            new_state, new_path = new_state
            new_state = tuple(set(new_state))
            new_g = g + 1
            new_f = new_g +( h(new_state, goals) * 1.5)
            if new_state not in visited:
                heapq.heappush(prioque, (new_f, new_g, new_state, new_path))
                visited.add(new_state)
    return None

def main(spec):
    X = len(spec)
    Y = len(spec[0])
    initial_state = []
    goals = []
    for i in range(X):
        for j in range(Y):
            if spec[i][j] == 'S' or spec[i][j] == 'B':
                initial_state.append((i, j))
            if spec[i][j] == 'B' or spec[i][j] == 'G':
                goals.append((i, j))
    state = lower_uncertanity(spec, initial_state)
    path = astar(spec, state, goals, heuristic_fn)
    return path


with open("zad_input.txt", encoding="utf-8") as fin, \
     open("zad_output.txt", "w", encoding="utf-8") as fout:
    spec = []
    for line in fin:
        spec.append(line.strip()) 
    e = main(spec)
    fout.write(e)