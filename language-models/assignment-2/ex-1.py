from transformers import AutoModelForCausalLM, AutoTokenizer
import random

model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

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
  for i in range(20):
      expr, result = generate_expression()
      prompt = f"{examples}\nNow, {expr} ="

      inputs = tokenizer(prompt, return_tensors="pt")
      output = model.generate(**inputs, max_new_tokens=2)

      output = tokenizer.decode(output[0])
      # print("DEBUG -----")
      # print(output)
      # print("----- end debug")
      output = output.split(" ")[-1]
      print("output: ", output)
      print("result: ", result)

      if int(output) == result:
        print("correct")
        accuracy += 1
  return accuracy / 20


examples = "\n".join([
    "2 + 3 = 5",
    "5 - 2 = 3",
    "4 * 3 = 12",
    "10 - 7 = 3",
    "8 + 1 = 9",
])
expr, result = generate_expression()
prompt = f"{examples}\nNow, {expr} ="



print(calculate_accuracy())
