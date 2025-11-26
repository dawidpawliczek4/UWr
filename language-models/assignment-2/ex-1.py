from transformers import AutoModelForCausalLM, AutoTokenizer
import random

model_name = "flax-community/papuGaPT2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def get_nth_expression(n, path="ex-1.txt"):
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if n >= len(lines):
        raise ValueError("Not enough lines in file")

    line = lines[n]                      # e.g. "2 + 3 = 5"
    expr, result = line.split("=")       # "2 + 3 ", " 5"
    expr = expr.strip()                  # "2 + 3"
    result = int(result.strip())         # 5

    return expr, result


def generate_expression():
    a, b = random.randint(0, 20), random.randint(0, 20)
    op = random.choice(['+', '-', '*'])
    expr = f"{a} {op} {b}"
    result = eval(expr)
    if result < 0:
        return generate_expression()
    return expr, result


def calculate_accuracy():
  accuracy = 0
  for i in range(100):
      expr, result = get_nth_expression(i)
      prompt = f"A person solves:\n{examples}\nNow, a person solves:\n{expr} ="

      inputs = tokenizer(prompt, return_tensors="pt")
      output = model.generate(**inputs, max_new_tokens=1, pad_token_id=tokenizer.eos_token_id)
      output = tokenizer.decode(output[0])
      # print("DEBUG -----")
      # print(output)
      # print("----- end debug")
      output = output.split(" ")[-1]
      # print("output: ", output)
      # print("true result: ", result)

      if int(output) == result:
        # print("correct")
        accuracy += 1

  return accuracy / 30


examples = "\n".join([
    "2 + 3 = 5",
    "5 - 2 = 3",
    "4 * 3 = 12",
    "10 - 7 = 3",
    "8 + 1 = 9",
])
expr, result = generate_expression()
print(calculate_accuracy())
