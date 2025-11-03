import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.nn import functional as F

model_name = 'flax-community/papuGaPT2'
device = 'cpu'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def generate_replies_multiple_return_best(tokenizer: AutoTokenizer, model: AutoModelForCausalLM, prompt: str) -> list[str]:
    encoded = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **encoded,
            max_new_tokens=50,
            temperature=0.8,
            repetition_penalty=1.2,
            top_p=0.90,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=20,
        )

    replies = []
    for output in outputs:
        decoded = tokenizer.decode(output, skip_special_tokens=True)
        reply = decoded[len(prompt) :].strip()
        replies.append(reply or "(no response)")



def generate_reply(question: str):
    encoded = tokenizer(question, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            **encoded,
            max_new_tokens = 25,
            do_sample = False
        )
        return output

def answer_czy(question: str):
    encoded = tokenizer(question, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **encoded,
            max_new_tokens = 10,
            do_sample = True,
        )
    yes_no = filter()
    # make that fun

def answer_ile(question: str):
    encoded = tokenizer(question, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **encoded,
            max_new_tokens = 10,
            do_sample = True,
        )
    number = filter()
    #make that fun


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
with open ("task4_answers.txt") as f:
    for line in f:
        answers.append(line.strip())

for question, answer in zip(questions, answers):
    print(question)
    print(answer)


def answer_question(question: str):
    if question.startswith("Ile"):
        return answer_ile(question)
    elif question.startswith("Czy"):
        return answer_czy(question)
    else:
        return generate_reply(question)


def answer_ile(question: str):
    pass

