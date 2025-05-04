# uzyjemy programowania dynamicznego, podobne do problemu 'word break'
# dp[i] przechowuje maksymalna osiagalna sume kwadratow dlugosci slow od poczatku do i
# prev[j] przechowuje indeks i, dla ktorego rozpoczelo sie slowo zakonczone na pozycji i, dzieki temu odtwrazamy podzial tekstu na slowa

with open("polish_words.txt", encoding="utf-8") as f:
    S = set(word.strip() for word in f.readlines())

def reconstruct_text(t, S):
    n = len(t)
    dp = [-float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    dp[0] = 0
    
    for i in range(n):
        if dp[i] == -float('inf'):
            continue
        for j in range(i+1, n+1):            
            if t[i:j] in S:                                
                candidate = dp[i] + (j - i) ** 2
                if candidate > dp[j]:
                    dp[j] = candidate
                    prev[j] = i
                        
    if dp[n] == -float('inf'):
        return None
        
    words = []
    pos = n
    while pos > 0:
        start = prev[pos]
        words.append(t[start:pos])
        pos = start
    words.reverse()
    return " ".join(words)
    
with open("pantad.txt", encoding="utf-8") as fin, \
     open("zad3_output_algo.txt", "w", encoding="utf-8") as fout:
    for line in fin:        
        t = line.strip()
        segmented = reconstruct_text(t, S)
        if segmented is not None:
            fout.write(segmented + "\n")
        else:
            fout.write("Brak możliwego podziału\n")
