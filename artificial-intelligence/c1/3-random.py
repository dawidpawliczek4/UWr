import random
from functools import lru_cache

def random_reconstruct_text(t, S):
    n = len(t)
    
    @lru_cache(maxsize=None)
    def ways(i):
        if i == n:
            return 1
        count = 0
        for j in range(i + 1, n + 1):
            if t[i:j] in S:
                count += ways(j)
        return count

    total = ways(0)
    if total == 0:
        return None 

    def pick_segmentation(i):
        if i == n:
            return []
        
        splits = []
        for j in range(i + 1, n + 1):
            if t[i:j] in S:
                splits.append((j, ways(j)))
        total_weight = sum(weight for _, weight in splits)
        r = random.uniform(0, total_weight)
        cumulative = 0
        for j, weight in splits:
            cumulative += weight
            if r <= cumulative: #przechodzimy przez wszystkie slowa i:j i dodajemy wage jak przekroczy randomowo wybrana to dodajemy
                return [t[i:j]] + pick_segmentation(j)
        return [] 

    segmentation = pick_segmentation(0)
    return " ".join(segmentation)

# Przykładowe użycie:
# Załaduj słownik z pliku "polish_words.txt"
with open("polish_words.txt", encoding="utf-8") as f:
    S = set(word.strip() for word in f.readlines())

# Przetwarzanie pliku wejściowego i zapis wyników do pliku wyjściowego
with open("pantad.txt", encoding="utf-8") as fin, \
     open("zad3_output_random.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        t = line.strip()
        segmented = random_reconstruct_text(t, S)
        if segmented is not None:
            fout.write(segmented + "\n")
        else:
            fout.write("Brak możliwego podziału\n")
