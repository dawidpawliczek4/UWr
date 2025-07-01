import random

def randperm(n):
    perm = list(range(n))
    for i in range(n - 1):
        j = random.randint(i, n - 1)
        perm[i], perm[j] = perm[j], perm[i]
    return perm

print(randperm(5))


## Fisher–Yates shuffle, Durstenfeld's version
