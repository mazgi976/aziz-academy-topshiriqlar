while True:
    s = input().split()
    
    if len(s) == 1:
        n = int(s[0])
        if n == 0:
            print("Exit")
            break  
    else:
        a, b = map(int, s)
        
        n = int(input())
        
    if n == 1:
        print(a + b)
    elif n == 2:
        print(a - b)
    elif n == 3:
        print(a * b)
    elif n == 4:
        print(a / b)