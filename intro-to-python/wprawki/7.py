import random
def sprawdz_wygrana(plansza):
    for i in range(3):
        countx = 0
        county = 0
        for j in range(3):
            if plansza[i][j] == 'X': 
                countx += 1
            if plansza[i][j] == 'O':
                county += 1             
        if countx == 3:
            return 'X'
        if county == 3:
            return 'O'
    for i in range(3):
        countx = 0
        county = 0
        for j in range(3):
            if plansza[j][i] == 'X': 
                countx += 1
            if plansza[j][i] == 'O':
                county += 1             
        if countx == 3:
            return 'X'
        if county == 3:
            return 'O'
    if plansza[0][0] == plansza[1][1] == plansza[2][2] == 'X':
        return 'X'
    if plansza[0][0] == plansza[1][1] == plansza[2][2] == 'O':
        return 'O'
    if plansza[0][2] == plansza[1][1] == plansza[2][0] == 'X':
        return 'X'
    if plansza[0][2] == plansza[1][1] == plansza[2][0] == 'O':
        return 'O'
        
        
    return 0



def symulacja(n):
    wygrane_x = 0
    wygrane_o = 0
    for i in range(n):
        tablica = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]        
        for i in range(9):
            poprawne = False
            while not poprawne:
                rand_x = random.randint(0, 2)
                rand_y = random.randint(0, 2)
                if tablica[rand_x][rand_y] == 0:
                    if i%2 == 0:
                        tablica[rand_x][rand_y] = 'X'
                    else:
                        tablica[rand_x][rand_y] = 'O'
                    poprawne = True
            czyWygralKtos = sprawdz_wygrana(tablica)
            if czyWygralKtos == 'X':
                wygrane_x += 1
                break
            elif czyWygralKtos == 'O':
                wygrane_o += 1
                break
    print("Prawdopodobienstwa:")
    print("Wygrana X:", wygrane_x/n)
    print("Wygrana O:", wygrane_o/n)
    print("Remis:", (n-wygrane_o-wygrane_x)/n)
                            
symulacja(10000)