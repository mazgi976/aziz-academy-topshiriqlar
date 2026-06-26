try:
    op = input().strip()
    a = float(input())
    b = float(input())
    
    if op == 'ADD':
        res = a + b
    elif op == 'SUB':
        res = a - b
    elif op == 'MUL':
        res = a * b
    elif op == 'DIV':
        res = a / b
    else:
         raise Exception()
                        
    print(f"{res:.2f}")
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")
except Exception:
    print("OPERR")            