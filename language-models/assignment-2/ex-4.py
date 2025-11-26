from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import torch.nn.functional as F
import math
import random

device = "cpu"

model_name = "flax-community/papuGaPT2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)


def log_probs_from_logits(logits, labels):
    logp = F.log_softmax(logits, dim=-1)
    logp_label = torch.gather(logp, 2, labels.unsqueeze(2)).squeeze(-1)
    return logp_label

def score_sentence(sentence_txt):
    input_ids = tokenizer(sentence_txt, return_tensors='pt')['input_ids'].to(device)
    with torch.no_grad():
        output = model(input_ids=input_ids)
        log_probs = log_probs_from_logits(output.logits[:, :-1, :], input_ids[:, 1:])
        seq_log_probs = torch.sum(log_probs)
    return float(seq_log_probs.cpu().numpy())


def filter_logits(logits, top_k, top_p, required_letter, tokenizer):
    probs = torch.softmax(logits, dim=-1)

    # wymuszanie słów zaczynających się na daną literę
    for tok_id in range(probs.size(0)):
        word = tokenizer.decode([tok_id])
        if word.strip() and word.strip()[0].isalpha(): # pozwalamy na cyfre?
            if word.strip()[0].lower() != required_letter.lower():
                probs[tok_id] = 0


    kth = torch.topk(probs, top_k).values.min()
    probs = torch.where(probs < kth, torch.zeros_like(probs), probs)

    sorted_probs, sorted_idx = torch.sort(probs, descending=True)
    cumulative = torch.cumsum(sorted_probs, dim=-1)
    mask = cumulative > top_p
    sorted_probs[mask] = 0
    probs = torch.zeros_like(probs).scatter(0, sorted_idx, sorted_probs)

    total = probs.sum()
    if total > 0:
        probs = probs / total
    else:
        probs = torch.softmax(logits, dim=-1)

    return probs


def generate_variant(prefix, target_letter, max_new_tokens=40):
    input_ids = tokenizer(prefix, return_tensors="pt").input_ids.tolist()[0]
    generated = list(input_ids)
    logps = []

    for _ in range(max_new_tokens):
        with torch.no_grad():
            out = model(torch.tensor([generated]))
            logits = out.logits[0, -1]

        probs = filter_logits(
            logits,
            top_k=40,
            top_p=0.92,
            required_letter=target_letter,
            tokenizer=tokenizer
        )

        dist = torch.distributions.Categorical(probs)
        next_id = int(dist.sample())

        logps.append(math.log(float(probs[next_id]) + 1e-12))
        generated.append(next_id)

        tok = tokenizer.decode([next_id])
        if tok in [".", "!", "?"]:
            break

    text = tokenizer.decode(generated)
    return text, logps


def score(text, logps):
    if not text.strip().endswith((".", "!", "?")):
        return -1e9

    words = text.strip().split()
    unique = set(words)

    repetition_penalty = len(words) - len(unique)

    # gwałtowne spadki log-prob
    drops = 0
    for i in range(1, len(logps)):
        if logps[i] < logps[i - 1] - 2.5:
            drops += 1

    avg_local = sum(logps) / len(logps)

    # globalna wiarygodność zdania
    global_score = score_sentence(text)

    return (
        # todo: dostosuj wagi
            avg_local
            + 0.001 * global_score
            - 1.3 * repetition_penalty
            - 2.0 * drops
    )


def main():
    prefiksy = []
    with open("prefiksy.txt") as f:
        for line in f:
            prefiksy.append(line.strip())

    prefix = random.choice(prefiksy)
    target_letter = prefix.split()[0][0].lower()

    variants = []
    for i in range(5):
        txt, logps = generate_variant(prefix, target_letter)
        variants.append((txt, score(txt, logps)))

    best_text, best_score = max(variants, key=lambda x: x[1])

    print("PREFIX:", prefix)
    print("BEST:\n", best_text)


if __name__ == "__main__":
    main()
