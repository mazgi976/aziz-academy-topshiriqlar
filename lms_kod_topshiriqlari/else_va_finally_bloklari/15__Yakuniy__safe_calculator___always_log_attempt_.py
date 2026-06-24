op = input()
a = input()
b = input()

attempts = 0
out = ''

try:
    a = float(a)
    b = float(b)
    
    if op == 'ADD':
        out = a + b
    elif op == 'SUB':
        out = a - b
    elif op == 'MUL':
        out = a * b
    elif op == 'DIV':
        out = a / b
    out = "{:.2f}".format(out)
    
except ValueError:
    out = 'BAD'
except ZeroDivisionError:
    out = 'DIV0'
finally:
    attempts += 1
    
print(out)
print(attempts)