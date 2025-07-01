from losowanie_fragmentow import losuj_fragment


def losuj_haslo(n):
    haslo = ""
    while len(haslo) != n:
        fragment = losuj_fragment()
        if len(haslo+fragment) > n or len(haslo+fragment) == n-1:
            continue
        else :
            haslo += fragment
    return haslo


for i in range(10):
    print(losuj_haslo(8))

for i in range(10):
    print(losuj_haslo(12))