
def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

ile = 0

for i in range(10,100000):
    if pierwsza(i):
        liczba = str(i)
        for i in range(0, len(liczba)-2):
            if liczba[i:i+3] == "777":
                print(liczba)
                ile += 1
                break

print("Ile liczb: ", ile)
