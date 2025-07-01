
def koperta(n):
    for i in range(2*n+1):
        print("*", end="")
    
    print()

    for i in range(n-1):
        wiersz = "*" + " " * i + "*" + " " * (2*n+1 - 2*i - 4) + "*" + " " * i + "*"
        print(wiersz)
    
    srodkowa = "*" + " " * ((2*n+1 - 3) // 2) + "*" + " " * ((2 * n + 1 - 3) // 2) + "*"
    print(srodkowa)
    
    for i in range(n-2, -1, -1):
        wiersz = "*" + " " * i + "*" + " " * (2*n+1 - 2*i - 4) + "*" + " " * i + "*"
        print(wiersz)

    for i in range(2*n+1):
        print("*", end="")
    
    print()


    
koperta(5)
