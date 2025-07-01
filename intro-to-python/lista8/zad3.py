from collections import Counter
from itertools import permutations

def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [word.strip().lower() for word in file.readlines()]

def is_valid_word(word, name_counter):
    return not (name_counter - Counter(word))

def find_word_pairs(name, words):
    name = name.replace(' ', '').lower()
    name_counter = Counter(name)
    valid_words = [word for word in words if is_valid_word(word, name_counter)]
    
    seen_pairs = set()
    for word1, word2 in permutations(valid_words, 2):
        combined = word1 + word2
        if Counter(combined) == name_counter:
            sorted_pair = tuple(sorted([word1, word2]))
            if sorted_pair not in seen_pairs:
                seen_pairs.add(sorted_pair)
                yield sorted_pair

def main():
    file_path = './popularne_slowa2023.txt'  # zmień na ścieżkę do pliku ze słowami
    name = "Czesław Miłosz"  # zmień na imię i nazwisko do testowania
    words = load_words(file_path)
    
    for pair in find_word_pairs(name, words):
        print(f"{pair[0]} {pair[1]}")

if __name__ == "__main__":
    main()
