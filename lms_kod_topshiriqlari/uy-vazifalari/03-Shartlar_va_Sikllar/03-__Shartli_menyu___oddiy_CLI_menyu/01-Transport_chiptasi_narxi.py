transport = int(input())
toifa = int(input())

if transport == 1 or transport == 2:
    narx = 1700
    if toifa == 1:
        print(narx)
    elif toifa == 2:
        print(narx // 2)
    elif toifa == 3:
        print(0)
    else:
        print("Notogri toifa")
elif transport == 3:
    narx = 4000
    if toifa == 1:
        print(narx)
    elif toifa == 2:
        print(narx // 2)
    elif toifa == 3:
        print(0)
    else:
        print("Notogri toifa")
else:
    print("Notogri transport")