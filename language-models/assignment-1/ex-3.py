import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.nn import functional as F

model_name = 'flax-community/papuGaPT2'
device = 'cpu'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

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


def predict_sentiment(review):
    prob_positive = sentence_prob("" + review + " Polecam.")
    prob_negative = sentence_prob("" + review + " Nie polecam.")
    if prob_positive > prob_negative:
        return "GOOD"
    else:
        return "BAD"



def main():
    with open("reviews_for_task3.txt") as f:
        reviews = f.readlines()
    reviews = [r.strip() for r in reviews if r.strip()]    
    reviews = [(r.split(' ', 1)[0], r.split(' ', 1)[1]) for r in reviews]    
    acc = 0
    counter = 0
    for pair in reviews:
        print("Review:", counter)
        counter += 1
        predicted = predict_sentiment(pair[1])
        if predicted == pair[0]:
            acc += 1
    print("Accuracy:", acc / len(reviews))



if __name__ == "__main__":
    main()