
def sito(n):
    pierwsze = list(range(n))
    pierwsze[0] = 0
    pierwsze[1] = 0
    for i in range(2, n):
        if pierwsze[i] != 0:
            for j in range(i+1, n):
                if pierwsze[j] % pierwsze[i] == 0:
                    pierwsze[j] = 0
    return pierwsze



def palindromiczne(a,b):
    palindromy = []
    pierwsze = sito(b+1)
    for i in range(a, b+1):
        if pierwsze[i] != 0:
            if str(i) == str(i)[::-1]:
                palindromy.append(i)
    return palindromy

print(palindromiczne(6,928))
print(palindromiczne(5,929))