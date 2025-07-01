def U2(n: int, k: int) -> str:
    if n >= 0:
        binarna = bin(n)[2:]
        while len(binarna) < k:
            binarna = '0' + binarna
        return binarna
    else:
        n = abs(n) - 1
        binarna = bin(n)[2:]
        while len(binarna) < k:
            binarna = '0' + binarna
        u2 = ''
        for bit in binarna:
            u2 += '1' if bit == '0' else '0'
        return u2

# Przykład użycia:
n = -5
k = 8
print(U2(n, k))
