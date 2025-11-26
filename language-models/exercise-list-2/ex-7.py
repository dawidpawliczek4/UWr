from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "flax-community/papuGaPT2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate(prefix):
    inputs = tokenizer(prefix, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=40,
            do_sample=True,
            temperature=0.8,
            top_p=0.9
        )
    return tokenizer.decode(output[0], skip_special_tokens=True)

tests = [
    "Dzisiaj idę do sklepu",
    "Moja dziewczyna bardzo lubi",
    "Wczoraj widziałem psa który",
    "Programowanie w Pythonie jest",
    "Kiedy byłem młodszy chciałem zostać",
]

for t in tests:
    print("=" * 80)
    print(f"Prefiks      : '{t}'")
    print(f"Prefiks + ' ' : '{t + ' '}'")
    print("\n--- Bez spacji na końcu ---")
    print(generate(t))
    print("\n--- Ze spacją na końcu ---")
    print(generate(t + " "))
