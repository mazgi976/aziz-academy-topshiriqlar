while True:
    amal = int(input())
    
    if amal == 0:
        break
        
    a = int(input())
    b = int(input())
    
    if amal == 1:
        print(a + b)
    elif amal == 2:
        print(a - b)
    elif amal == 3:
        print(a * b)
    elif amal == 4:
        if b == 0:
            print("Xato")
        else:
            print(a // b)
    else:
        print("Noma'lum")