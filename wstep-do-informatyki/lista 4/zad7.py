

def kcyfrowy(n):
    n = str(n)
    liczby = []
    for i in n:
        if i not in liczby:
            liczby.append(i)
    return len(liczby)

print(kcyfrowy(73737))
