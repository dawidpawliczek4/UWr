from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer, util
import torch


MODEL_NAME = "flax-community/papuGaPT2"


# here we using semantic score, idk if in scope of task
emb_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
def semantic_score(prompt: str, reply: str) -> float:
    emb1 = emb_model.encode(prompt, convert_to_tensor=True)
    emb2 = emb_model.encode(reply, convert_to_tensor=True)
    return float(util.cos_sim(emb1, emb2))
def hybrid_score(prompt: str, reply: str) -> float:
    return score(reply)
    return semantic_score(prompt, reply) * 0.7 + score(reply) * 0.3



def load_model_and_tokenizer(model_name: str = MODEL_NAME):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()
    return tokenizer, model

def score(output: str) -> float:
    score = 0
    alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZąćęłńóśźżĄĆĘŁŃÓŚŹŻ ")
    for char in output:
        if char in alphabet:        
            score += 2
        if char in ".,!?-":
            score += 1
        else:
            score -= 100
    return score


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

    replies = sorted(replies, key=lambda r: hybrid_score(prompt, r), reverse=False)
    return replies[-1]


# def generate_reply(tokenizer: AutoTokenizer, model: AutoModelForCausalLM, prompt: str) -> str:
#     encoded = tokenizer(prompt, return_tensors="pt")

#     with torch.no_grad():
#         output = model.generate(
#             **encoded,
#             max_new_tokens=20,            
#             temperature=0.8,
#             repetition_penalty=1.2, 
#             top_p=0.90,
#             do_sample=True,
#             pad_token_id=tokenizer.eos_token_id,
#         )

#     decoded = tokenizer.decode(output[0], skip_special_tokens=True)
#     reply = decoded[len(prompt) :].strip()
#     return reply or "(no response)"


CTX = (
    "Rozmowa pomiędzy użytkownikiem i asystentem."
    "Asystent jest pomocny, rzeczowy i odpowiada zwięźle po polsku."
    "Użytkownik zadaje pytania, a asystent udziela prostych, klarownych odpowiedzi."
    # "Przykład:"
    # "Użytkownik: Co to jest fotosynteza?"
    # "Asystent: Fotosynteza to proces, w którym rośliny zamieniają energię światła słonecznego w energię chemiczną."
)



def main() -> None:
    tokenizer, model = load_model_and_tokenizer()
    history = []

    while True:
        try:
            prompt = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if prompt == "!reset":
            history = []
            print("Historia rozmowy została zresetowana. \n\n")
            continue

        prompt = f"Użytkownik: {prompt} Asystent: "
        prompt_with_hist = CTX + "".join(history + [prompt])

        # print("[DEBUG] prompt_with_hist:", prompt_with_hist + "[END_DEBUG] + ")

        reply = generate_replies_multiple_return_best(tokenizer, model, prompt_with_hist)
        history += [prompt + f"{reply}. "]
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()
