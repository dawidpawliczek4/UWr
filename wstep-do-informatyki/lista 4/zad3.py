
def gcd_list(lista):
    minimum = min(lista)
    current_gcd = 1
    for i in range(minimum, 1, -1):
        czyNoweGcd = True
        for el in lista:
            if el % i != 0:
                czyNoweGcd = False                
        if czyNoweGcd:
            current_gcd = i
            break
    return current_gcd

        


print(gcd_list([12,4,3]))