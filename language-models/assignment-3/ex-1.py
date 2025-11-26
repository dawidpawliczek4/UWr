import torch
from transformers import AutoModel, AutoTokenizer

model_name = 'allegro/herbert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


def get_static_embedding_for_word(word):
    token_ids = tokenizer.encode(word, add_special_tokens=False)

    # Konwersja na tensor PyTorch i dodanie wymiaru partii (batch dimension)
    input_ids = torch.tensor(token_ids).unsqueeze(0)

    # Wyciągnięcie wektorów z "Tabeli" (Lookup Table)
    with torch.no_grad():
        # Pobieramy wektory dla każdego pod-tokenu
        raw_embeddings = model.embeddings.word_embeddings(input_ids)
        # raw_embeddings ma kształt: [1, liczba_tokenow, 768] (dla base model)

    # 4. Uśrednianie (Mean Pooling)
    # dim=1 oznacza, że uśredniamy wzdłuż sekwencji tokenów
    word_embedding = torch.mean(raw_embeddings, dim=1).squeeze().numpy()

    return word_embedding


# Przykład użycia
word = "nierozerwalny"  # "nierozerwalny"
vec = get_static_embedding_for_word(word)

print(f"Słowo: {word}")
print(f"Wymiar wektora: {vec.shape}")  # Powinno być (768,)
print(f"Pierwsze 5 liczb: {vec[:5]}")