import string

def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Usuwanie interpunkcji
    text = text.translate(str.maketrans('', '', string.punctuation + '—'))

    # Zamiana wszystkich liter na małe
    text = text.lower()

    # Usunięcie nadmiarowych przejść do nowej linii
    text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Przykład użycia
input_file = 'pantad_original.txt'  # Podaj nazwę pliku wejściowego
output_file = 'pantad_orig_cleaned.txt' # Podaj nazwę pliku wyjściowego
clean_text(input_file, output_file)
print(f'Przetworzony tekst zapisano w pliku: {output_file}')
