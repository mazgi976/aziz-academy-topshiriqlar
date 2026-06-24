try:
    op = input()
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
        print('OPERR')
        exit()
                        
    print(f"{res:.2f}")
    
except ValueError:
    print('BAD')
except ZeroDivisionError:
    print('DIV0')