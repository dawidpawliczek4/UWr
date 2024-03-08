

def value(a, k):
    w = 0
    for i in range(k+1):
        w = w + a[i]* 2**i
    return w


ret = value([1,1,0,1], 3)
print(ret)