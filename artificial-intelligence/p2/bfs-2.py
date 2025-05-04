import collections

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

# state: ( (x,y), 'LLLLLRR...' )
def bfs(spec, state):
    pos, path = state
    state = pos
    queue = collections.deque([(state, path)])
    visited = {state}

    while queue:
        st, path = queue.popleft()
        # if spec[pos[0]][pos[1]] == "B" or spec[pos[0]][pos[1]] == 'G':
        #     return path

        if all(spec[pos[0]][pos[1]] == 'B' or spec[pos[0]][pos[1]] == 'G' for pos in st):
            return path
        
        new_states = generate_moves(spec, st, path)
        
        for new_state, new_path in new_states:
            if tuple(new_state) in visited:
                continue
            queue.append((new_state, new_path))    
            visited.add(tuple(new_state))

def main(spec):
    X = len(spec)
    Y = len(spec[0])
    initial_state = []
    for i in range(X):
        for j in range(Y):
            if spec[i][j] == 'S' or spec[i][j] == 'B':
                initial_state.append((i, j))
    state = lower_uncertanity(spec, initial_state)
    path = bfs(spec, state)
    return path


with open("zad_input.txt", encoding="utf-8") as fin, \
     open("zad_output.txt", "w", encoding="utf-8") as fout:
    spec = []
    for line in fin:
        spec.append(line.strip()) 
    
    e = main(spec)
    fout.write(e)