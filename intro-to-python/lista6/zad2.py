
file = []

with open('./popularne_slowa2023.txt') as f:
    for l in f:
        file.append(l.strip())


slowa = {}

for slowo in file:
    odwroconeSlowo = slowo[::-1]

    if odwroconeSlowo in slowa:
        print(slowo, odwroconeSlowo)
    else:
        slowa[slowo] = 1