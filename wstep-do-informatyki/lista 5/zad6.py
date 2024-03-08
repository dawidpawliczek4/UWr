
def fibonacci(k ,r):
    if k == 1 or k == 0:
        return 1
    fibos = [1, 1]
    for i in range(2, k+1):
        fibos.append(( fibos[i-1]%r + fibos[i-2]%r ) % r)
    
    print(fibos)

fibonacci(10, 3)