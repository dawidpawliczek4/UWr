def relacja_rown(elem):
    if not elem:
        return [[]]
    rez = []
    first = elem[0]
    for smaller in relacja_rown(elem[1:]):
        for n, subset in enumerate(smaller):
            rez.append(smaller[:n] + [[first] + subset] + smaller[n+1:])
        rez.append([[first]] + smaller)
    return rez

elements = [1, 2, 3, 4]
print(relacja_rown(elements))