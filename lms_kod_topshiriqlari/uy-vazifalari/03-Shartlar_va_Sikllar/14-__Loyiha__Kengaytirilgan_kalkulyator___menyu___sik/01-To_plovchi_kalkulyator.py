natija = 0

while True:
    belgi = input()
    
    if belgi == "=":
        print(natija)
        break
        
    son = int(input())
    
    if belgi == '+':
        natija += son
    elif belgi == '-':
        natija -= son
    elif belgi == '*':
        natija *= son
    elif belgi == '/':
        if son != 0:
            natija //= son