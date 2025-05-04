import random

def random_reconstruct_text_uniform(t, S):
    n = len(t)
    
    def helper(i):
        # Gdy doszliśmy do końca tekstu, zwracamy pustą listę (sukces)
        if i == n:
            return []
        # Generujemy listę indeksów końca słowa j, dla których t[i:j] jest poprawnym słowem
        candidates = [j for j in range(i + 1, n + 1) if t[i:j] in S]
        if not candidates:
            # Brak możliwości podziału od pozycji i
            return None
        
        # Losujemy kolejność kandydatów (każdy ma równą szansę bycia sprawdzonym jako pierwszy)
        random.shuffle(candidates)
        
        # Próbujemy rekurencyjnie każdy z losowo uporządkowanych kandydatów
        for j in candidates:
            rest = helper(j)
            if rest is not None:
                # Gdy udało się zrekonstruować resztę tekstu, łączymy bieżące słowo z wynikiem
                return [t[i:j]] + rest
        # Jeżeli żaden kandydat nie prowadzi do poprawnego segmentu, zwracamy None
        return None
    
    segmentation = helper(0)
    return " ".join(segmentation) if segmentation is not None else None


# Przykładowe użycie:
# Załaduj słownik z pliku "polish_words.txt"
with open("polish_words.txt", encoding="utf-8") as f:
    S = set(word.strip() for word in f.readlines())

# Przetwarzanie pliku wejściowego i zapis wyników do pliku wyjściowego
with open("pantad.txt", encoding="utf-8") as fin, \
     open("zad3_output_random-jednolite.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        t = line.strip()
        segmented = random_reconstruct_text_uniform(t, S)
        if segmented is not None:
            fout.write(segmented + "\n")
        else:
            fout.write("Brak możliwego podziału\n")
