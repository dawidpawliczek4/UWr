from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "eryk-mazus/polka-1.1b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def translate(sentence: str):
    prompt = f"""
English: {sentence}
Polish:
"""
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=30, temperature=0.7, top_p=0.95)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    translated = result.split("Polish:")[-1].strip()
    return translated


correct_sentence = "I have a dog."
wrong_sentence = "The book is on the table."

print("✅ Correct example:")
print(f"English: {correct_sentence}")
print(f"Polish:  {translate(correct_sentence)}\n")

print("❌ Possible incorrect example:")
print(f"English: {wrong_sentence}")
print(f"Polish:  {translate(wrong_sentence)}")
