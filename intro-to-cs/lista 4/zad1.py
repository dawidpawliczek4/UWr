def a(n):
    if n % 2 == 0:
        return n
    return -n

def b(n):
    suma = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            suma += 1/i
        else:
            suma -= 1/i
    return suma

def c(n, x):
    suma = 0
    potega_x = x
    for i in range(1, n+1):
        suma += i * potega_x
        potega_x = potega_x * x
    return suma