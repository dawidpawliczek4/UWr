import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.nn import functional as F
import itertools

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

def sort_by_prob(sentence: list[int]) -> list[int]:
    print("Generating permutations for sentence")
    
    sentence = [word.lower() for word in sentence]
    # strip . from all words
    sentence = [word.strip('.,!?-') for word in sentence]

    all_perms = itertools.permutations(sentence)

    sentences = [' '.join(p) for p in all_perms]    

    # for every sentence in sentences, make first letter uppercase, add . to sentence
    sentences = [s[0].upper() + s[1:] + '.' for s in sentences]
    
    scores = [(sentence_prob(p), p) for p in sentences ]
    scores.sort(reverse=True, key=lambda x: x[0])
    return scores

test_sentences = [
#   ['This', 'is', 'a', 'normal', 'English', 'sentence.'],
  'W tym roku pogoda jest ładna.'.split(' '),
]

for sentence in test_sentences:
    res = sort_by_prob(sentence)
    print(res)




