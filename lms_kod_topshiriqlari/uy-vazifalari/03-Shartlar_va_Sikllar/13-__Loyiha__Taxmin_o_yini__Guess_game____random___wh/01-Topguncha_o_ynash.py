yashirin_son = int(input())
urinishlar = 0

while True:
    taxmin = int(input())
    urinishlar += 1
    
    if taxmin == yashirin_son:
        print("TOPDINGIZ")
        break
    elif taxmin > yashirin_son:
        print("KATTA")
    else:
        print("KICHIK")
        
print(f"Urinishlar: {urinishlar}")