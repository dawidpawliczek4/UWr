

def find_smallest_k(n, m):
    k = 0
    while n ** k < m:
        k += 1
    return k
