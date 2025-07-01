def kolko(n):
    ile=0
    srodek=0

    if (n // 2) % 2 == n%2:  # np 7, bo 7//2 = 3 oby dwa sa np wiec git
        srodek = "#" * n + "\n"
        srodek = srodek * (n // 2)
        ile = n - (n // 2)
        
    else: # np 6, bo 6//2=3, 3 jest np a 6 p wiec musimy odejmnac 1
        srodek = "#" * n + "\n"
        srodek = srodek * (n//2 - 1)
        
        ile = n - (n//2 - 1)

    dol = []

    for i in range(n-2, n-2-(ile), -2):
            # print(n, i)
            spacje = " " * ((n-i) // 2)
            hash = "#" * i
            dol.append(spacje + hash + "\n")
            
    gora = dol[::-1]

    print(''.join(gora), end="")
            
    print(srodek, end="")
            
    print(''.join(dol))

kolko(15)

def kolko_drugie(n, ile_spacji_dodac):
     
    if (n // 2) % 2 == n%2:  # np 7, bo 7//2 = 3 oby dwa sa np wiec git
        srodek = " " * ile_spacji_dodac + "#" * n + "\n"
        srodek = srodek * (n // 2)
        ile = n - (n // 2)
        
    else: # np 6, bo 6//2=3, 3 jest np a 6 p wiec musimy odejmnac 1
        srodek = " " * ile_spacji_dodac + "#" * n + "\n"
        srodek = srodek * (n//2 - 1)        
        ile = n - (n//2 - 1)

    dol = []

    for i in range(n-2, n-2-(ile), -2):
            spacje = " " * ile_spacji_dodac + " " * ((n-i) // 2) 
            hash = "#" * i
            dol.append(spacje + hash + "\n")
            
    gora = dol[::-1]

    print(''.join(gora), end="")
            
    print(srodek, end="")
            
    print(''.join(dol), end="")
     

kolko_drugie(5, 2)     
kolko_drugie(7, 1)
kolko_drugie(15, 0)
