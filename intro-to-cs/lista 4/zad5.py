def czyPalindromBinarny(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False



def czyPalindromBinarny2(n):
    n = str(n)
    dlugosc = len(n)
    srodek = dlugosc // 2
    for i in range(srodek):
        if n[i] == n[dlugosc-1 - i]:
            continue
        return False
    return True

print(czyPalindromBinarny2(101))