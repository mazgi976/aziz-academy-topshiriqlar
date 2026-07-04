yashirin_son = int(input())
n = int(input())
topildi = False

for i in range(n):
    taxmin = int(input())
    if taxmin == yashirin_son:
        print("TOPDINGIZ")
        topildi = True
        break
    elif taxmin > yashirin_son:
        print("KATTA")
    else:
        print("KICHIK")
        
if not topildi:
    print("YUTQAZDINGIZ")