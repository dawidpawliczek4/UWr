silnia_wartosci = []

n = 100

najwieksza_silnia_val = 1

i_2 = 0

while najwieksza_silnia_val < n:
    i_2 += 1
    najwieksza_silnia_val = najwieksza_silnia_val * i_2
    silnia_wartosci.append(najwieksza_silnia_val)


silniowa_rep_val = 0
silniowa_rep = []

for i in range(i_2-1, -1, -1):

    silnia_i = silnia_wartosci[i]

    if silniowa_rep_val != n:
        for s in range(i+1, -1, -1):
            if (s) * silnia_i + silniowa_rep_val <= n:
                silniowa_rep.append(s)
                silniowa_rep_val+= (s)*silnia_i
                break
    else:
        silniowa_rep.append(0)
    

while silniowa_rep and silniowa_rep[0] == 0:
    silniowa_rep.pop(0)

    

print(silniowa_rep, silniowa_rep_val)