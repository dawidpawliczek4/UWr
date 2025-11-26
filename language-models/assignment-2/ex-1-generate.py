import random

def generate_expression():
    a, b = random.randint(0, 20), random.randint(0, 20)
    op = random.choice(['+', '-', '*'])
    expr = f"{a} {op} {b}"
    result = eval(expr)
    if result < 0:
        return generate_expression()
    return expr, result

for i in range(1000):
    expr, result = generate_expression()
    line = f"{expr} = {result}"
    #write line to ex-1.txt file
    with open("./ex-1.txt", "a") as f:
        f.write(line + "\n")