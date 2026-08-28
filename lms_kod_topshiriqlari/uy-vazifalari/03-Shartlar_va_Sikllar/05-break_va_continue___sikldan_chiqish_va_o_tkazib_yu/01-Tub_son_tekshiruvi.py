n = int(input())

if n <= 1:
    print("yo'q")
else:
    tub = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tub = False
            break
            
    if tub:
        print("ha")
    else:
        print("yo'q")