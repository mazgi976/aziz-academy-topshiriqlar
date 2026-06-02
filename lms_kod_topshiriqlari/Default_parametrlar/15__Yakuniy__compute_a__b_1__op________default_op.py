def compute(a, b=1, op='+'):
    if op == '/':
        if b == 0:
            return "ERROR"
        return a / b
    elif op == '+':
        return a + b 
    elif op == '-':
        return a - b 
    elif op == '*':
        return a * b

tokens = input().split()

if len(tokens) == 1:
    res = compute(int(tokens[0]))
elif len(tokens) == 2:
    res = compute(int(tokens[0]), int(tokens[1]))
else:
    res = compute(int(tokens[0]), int(tokens[1]), tokens[2])
    
if res == "ERROR":
    print("ERROR")
elif isinstance(res, float):
    print(f"{res:.2f}")
else:
    print(res)