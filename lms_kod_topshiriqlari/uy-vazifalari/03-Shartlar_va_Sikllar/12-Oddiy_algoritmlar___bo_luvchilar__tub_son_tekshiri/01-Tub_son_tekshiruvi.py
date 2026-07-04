n = int(input())

if n <= 1:
    print("TUB EMAS")
else:
    is_tub = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_tub = False
            break
            
    if is_tub:
        print("TUB")
    else:
        print("TUB EMAS")