
def krzyzyk(n):
    for i in range(n):        
        print(" " * (n - 1), "*" * n)
    for i in range(n):
        print("*" * 3 * n)
    for i in range(n):
        print(" " * (n - 1), "*" * n)        

krzyzyk(4)
