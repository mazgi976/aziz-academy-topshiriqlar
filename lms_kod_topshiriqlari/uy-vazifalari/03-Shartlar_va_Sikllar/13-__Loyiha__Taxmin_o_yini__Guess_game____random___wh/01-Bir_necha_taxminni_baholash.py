yashirin_son = int(input())
k = int(input())

for i in range(k):
    taxmin = int(input())
    if taxmin == yashirin_son:
        print("TOPDINGIZ")
    elif taxmin > yashirin_son:
        print("KATTA")
    else:
        print("KICHIK")