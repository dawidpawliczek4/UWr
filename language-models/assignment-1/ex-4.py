import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.nn import functional as F
import re

model_name = 'flax-community/papuGaPT2'
device = 'mps'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def generate_reply(question: str):
    encoded = tokenizer(question, return_tensors="pt").to(device)
    with torch.no_grad():
        output = model.generate(
            **encoded,
            max_new_tokens = 5,
            do_sample = False,
            pad_token_id=tokenizer.eos_token_id,
        )
        return output

def answer_czy(question: str):
    p_tak = sentence_prob(question + " tak")
    p_nie = sentence_prob(question + " nie")

    return "tak" if p_tak > p_nie else "nie"


def answer_ile(question: str):
    """Generuje odpowiedź liczbową i wybiera pierwszą liczbę z generacji."""
    encoded = tokenizer(question, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **encoded,
            max_new_tokens=2,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=5,
        )

    candidates = []
    for output in outputs:
        decoded = tokenizer.decode(output, skip_special_tokens=True)
        reply = decoded[len(question):].strip()
        candidates.append(reply)

    # Heurystyka: znajdź pierwszą liczbę w wygenerowanym tekście
    for cand in candidates:
        match = re.search(r'\d+', cand)
        if match:
            return match.group(0)

    return "(brak liczby)"


def log_probs_from_logits(logits, labels):
    logp = F.log_softmax(logits, dim=-1)
    logp_label = torch.gather(logp, 2, labels.unsqueeze(2)).squeeze(-1)
    return logp_label


def sentence_prob(sentence_txt):
    input_ids = tokenizer(sentence_txt, return_tensors='pt')['input_ids'].to(device)
    with torch.no_grad():
        output = model(input_ids=input_ids)
        log_probs = log_probs_from_logits(output.logits[:, :-1, :], input_ids[:, 1:])
        seq_log_probs = torch.sum(log_probs)
    return seq_log_probs.cpu().numpy()

def answer_question(question: str):
    if question.startswith("Ile"):
        return answer_ile(question)
    elif question.startswith("Czy"):
        return answer_czy(question)
    else:
        return generate_reply(question)


questions: list[str] = []
with open("task4_questions.txt") as f:
    for line in f:
        questions.append(line.strip())

# for question in sorted(questions):
#     print(question)
"""
1. grupa 'ile' - odpowiadamy liczba. nasza heura to poprostu branie liczby z mozliwcyh odpwoeidzi papugi
2. grupa 'czy' - odpwoaidamy tak/nie. bedziemy obliczac ppb prompt+'tak' i ppb prompt+'nie'
"""

answers: list[str] = []
with open("task4_answers.txt") as f:
    for line in f:
        answers.append(line.strip())

good_ans = 0

for question, answer in zip(questions, answers):
    model_ans = answer_question(question)
    if model_ans == answer:
        good_ans += 1

print(good_ans)
print(len(questions))
print(good_ans / len(questions))


