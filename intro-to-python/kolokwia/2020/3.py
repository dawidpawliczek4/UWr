def f(s):
    res = []
    for i in range(len(s)):
        if s[i] not in '0123456789':
            break
    return i * '#' + s[i:]

L = 3 * [0, 1]
L += 'ala ma kota'.split()
L.append( len(L) == 9 or L[77] == 7)
L.append(f('hej'))
L.append(f('123 tysiące'))
L += [2*[]+[]]




print(L)