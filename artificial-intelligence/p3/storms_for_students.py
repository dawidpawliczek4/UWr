def B(i,j):
    return 'B_%d_%d' % (i,j)

def all_different(Qs):
    return 'all_distinct([' + ', '.join(Qs) + '])'

def get_col(j, C):
    return [B(c, j) for c in range(C)]

def get_row(i, R):
    return [B(i, r) for r in range(R)]

def domains(bs):
    return [ q + ' in 0..1,' for q in bs ]

def known(triples):
    return [rf"{B(u[0], u[1])} #= {u[2]}," for u in triples]

def rows_sum(n, m, rows):
    cs = []
    for i in range(n):
        cs += ['(' + ' + '.join(get_row(i, n)) + ')' + ' #= ' + str(rows[i]) + ',']
    return cs

def cols_sum(n, m, cols):
    cs = []
    for i in range(m):
        cs += ['(' + ' + '.join(get_col(i, m)) + ')' + ' #= ' + str(cols[i]) + ',']
    return cs

# B => (A or C)
def impl(lista):
    return rf"{lista[1]} #==> ({lista[0]} #\/ {lista[2]}),"

def get_3_cons(lista):
    return [[lista[i + j] for j in range(3)] for i in range(0, len(lista) - 2)]

def cons_3_rows(n, m):
    cs = []
    for i in range(n):
        cs += map(impl, get_3_cons(get_row(i, n)))
    return cs
        
def cons_3_cols(n, m):
    cs = []
    for i in range(m):
        cs += map(impl, get_3_cons(get_col(i, m)))
    return cs

# AB
# CD
# A and D  =>  B and C
def get_2x2(n, m):
    l = []
    for i in range(n - 1):
        for j in range(m - 1):
            l.append([B(i, j), B(i, j + 1), B(i + 1, j), B(i + 1, j + 1)])
    return l

def impl_matrix(l):
    return rf"({l[0]} #/\ {l[3]}) #<==> ({l[1]} #/\ {l[2]}),"

def check2x2(n, m):
    return map(impl_matrix, get_2x2(n, m))


    
def storms(rows, cols, triples):
    writeln(':- use_module(library(clpfd)).')
    
    n = len(rows)
    m = len(cols)
    
    bs = [ B(i,j) for i in range(n) for j in range(m)]
    
    writeln('solve([' + ', '.join(bs) + ']) :- ')

    #TODO: add some constraints
    
    cs = domains(bs)
    cs += known(triples)
    cs += rows_sum(n, m, rows)
    cs += cols_sum(n, m, cols)
     
    # dla kazdej trojki [A,B,C]
    # B => (A or C)
    # oraz analogicznie w pionie
    cs += cons_3_rows(n, m) + cons_3_cols(n, m)
        
    #   [AB]
    #   [CD]
    # A i D sa ustawione na 1 wtw gdy B i C tez
    # nie moze byc
    # 1 0
    # 0 1
    #zeby nie stykaly sie rogami
    cs += check2x2(n, m)

    output.write('\n'.join(cs) + '\n')    
    writeln('labeling([ff], [' +  ', '.join(bs) + ']).' )
    writeln('')
    writeln(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")

def writeln(s):
    output.write(s + '\n')

txt = open('zad_input.txt').readlines()
output = open('zad_output.txt', 'w')

rows = list(map(int, txt[0].split()))
cols = list(map(int, txt[1].split()))
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(list(map(int, txt[i].split())))

storms(rows, cols, triples)            
        