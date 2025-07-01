from duze_cyfry import daj_cyfre

# za 0.5 pkt

# liczba = input()
# liczba = [int(i) for i in liczba]

# for i in liczba:
#     for r in daj_cyfre(i):
#         print(r)


## za 1pkt

liczba = input()
liczba = [int(i) for i in liczba]

for r in range(5):  
    for i in liczba:
        print(daj_cyfre(i)[r], end=" ")
    print()  