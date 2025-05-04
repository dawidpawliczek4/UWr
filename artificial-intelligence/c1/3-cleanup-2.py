import re

def clean_text(text):
    text = re.sub(r' {2,}', ' ', text)
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'[…»]', '', text)  # Usuwa znaki … i »
    text = '\n'.join(line.strip() for line in text.split('\n'))
    return text.strip()

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = clean_text(text)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

# Przykład użycia
input_path = 'pantad_orig_cleaned.txt'
output_path = 'pantad_orig_cleaned.txt'
process_file(input_path, output_path)
print(f'Przetworzono plik: {input_path} -> {output_path}')
