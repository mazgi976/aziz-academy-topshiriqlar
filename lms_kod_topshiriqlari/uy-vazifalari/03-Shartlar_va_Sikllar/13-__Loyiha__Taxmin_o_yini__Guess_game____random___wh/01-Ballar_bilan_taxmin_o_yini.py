yashirin_son = int(input())
ball = 100

while True:
    taxmin = int(input())
    
    if taxmin == yashirin_son:
        print("TOPDINGIZ")
        print(f"Ball: {ball}")
        break
    else:
        if taxmin > yashirin_son:
            print("KATTA")
        else:
            print("KICHIK")
            
        ball = max(0, ball - 10)