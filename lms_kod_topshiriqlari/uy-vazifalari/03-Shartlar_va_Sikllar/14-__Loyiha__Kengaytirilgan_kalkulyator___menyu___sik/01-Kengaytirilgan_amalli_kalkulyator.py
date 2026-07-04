eng_katta = None

while True:
    k = int(input())
    if k == 0:
        break
        
    a = int(input())
    b = int(input())
    
    res = None
    
    if k == 1:
        res = a + b
    elif k == 2:
        res = a - b
    elif k == 3:
        res = a * b
    elif k == 4:
        if b != 0:
             res = a // b
    elif k == 5:
        res = a ** b
    elif k == 6:
        if b != 0:
            res = a % b
            
    if res is not None:
        print(res)
        if eng_katta is None or res > eng_katta:
            eng_katta = res
            
if eng_katta is not None:
    print(f"Eng katta natija: {eng_katta}")