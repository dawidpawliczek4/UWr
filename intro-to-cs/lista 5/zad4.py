

def wyznaczG(n):
    gn = 1
    gn1 = 1
    gn2 = 1
    gn3 = 1
    for i in range(3, n+1):
        gn = gn1 + gn2 + gn3
        gn3 = gn2
        gn2 = gn1
        gn1 = gn
    return(gn)


print(wyznaczG(10))