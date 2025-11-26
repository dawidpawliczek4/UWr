from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torch.nn.functional as F

model_name = "flax-community/papuGaPT2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
device = "cpu"

def pick_best(beams: list[tuple[str, float]], n: int) -> list[tuple[str, float]]:
    beams.sort(key=lambda x: x[1], reverse=True)
    return beams[:n]

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
    return seq_log_probs.cpu().numpy()


variants = [
    ["wprost", "wyprosty", "wyprostu", "wyprost"],
    ["uwielbiała", "wielbił", "wielbiła", "uwielbił", "wielbiło", "uwielbiał", "uwielbiało", "uwielbiały"],
    ["słuchać", "osłuchać", "słychać", "usłuchać"],
    ["o", "i", "e", "a", "ó", "ę", "y", "ą", "u"],
    ["wartościach" ] ,
    [ "własnych", "owłosionych" ],
    [ "macierzy", "mocarz", "macierzą", "macierze", "mocarza", "mocarze", "mocarzy", "macierz"]
]

beam_size = 2
beams = [("", 0)]  # zdanie, wynik
for list_variants in variants:
    new_beams = []
    for (sentence, score) in beams:
        for word in list_variants:
            new_sentence = sentence + " " + word
            new_score = score_sentence(new_sentence)
            new_beams.append((new_sentence, new_score))
    beams = pick_best(new_beams, n=beam_size)

# na końcu najlepsze zdanie:
print(beams[0][0])
print(beams[0][1])
