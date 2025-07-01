def zmien_na_podstawe(liczba, podstawa):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wynik = ""
    while liczba > 0:
        reszta = liczba % podstawa
        wynik = digits[reszta] + wynik
        liczba = liczba // podstawa
    return wynik

def czy_palindrom(s):
    return s == s[::-1]

def czy_k_arny_palindrom(n, k):
    base_k_num = zmien_na_podstawe(n, k)
    return czy_palindrom(base_k_num)