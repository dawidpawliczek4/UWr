import sys

def V(i, j):
    return 'V%d_%d' % (i, j)

def domains(Vs):
    return [ q + ' in 1..9' for q in Vs ]

def all_different(Qs):
    return 'all_distinct([' + ', '.join(Qs) + '])'

def get_column(j):
    return [ V(i, j) for i in range(9) ]

def get_raw(i):
    return [ V(i, j) for j in range(9) ]

def horizontal():
    return [ all_different(get_raw(i)) for i in range(9) ]

def vertical():
    return [ all_different(get_column(j)) for j in range(9) ]

def squares():
    blocks = []
    for r in (0, 3, 6):
        for c in (0, 3, 6):
            blk = [ V(i, j) for i in range(r, r+3) for j in range(c, c+3) ]
            blocks.append(all_different(blk))
    return blocks

def print_constraints(Cs, indent, d, out):
    pos = indent
    out.write(indent * ' ')
    for c in Cs:
        out.write(c + ', ')
        pos += len(c)
        if pos > d:
            pos = indent
            out.write('\n' + indent * ' ')

def sudoku(assignments, out):
    vars_ = [ V(i,j) for i in range(9) for j in range(9) ]

    out.write(':- use_module(library(clpfd)).\n')
    out.write('solve([' + ', '.join(vars_) + ']) :-\n')

    cs = domains(vars_) + vertical() + horizontal() + squares()
    for i, j, val in assignments:
        cs.append(f'{V(i,j)} #= {val}')

    print_constraints(cs, 4, 70, out)
    out.write('\n')
    out.write('    labeling([ff], [' + ', '.join(vars_) + ']).\n\n')
    out.write(':- solve(X), write(X), nl.\n')

if __name__ == '__main__':
    triples = []
    raw = 0
    with open('zad_input.txt', 'r') as inp:
        for line in inp:
            line = line.strip()
            if len(line) == 9:
                for col, ch in enumerate(line):
                    if ch != '.':
                        triples.append((raw, col, int(ch)))
                raw += 1

    with open('zad_output.txt', 'w') as out:
        sudoku(triples, out)
