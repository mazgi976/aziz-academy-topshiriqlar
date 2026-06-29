try:
    kind = input().strip()
    a = int(input())
    b = int(input())
    
    if kind == "RECT":
        if a > 0 and b > 0:
            print(a * b)
        else:
            print("BAD")
    elif kind == "CIRCLE":
        if a > 0:
            print(int(3.14 * a * a))
        else:
            print("BAD")
    else:
        print("BAD")
except ValueError:
    print("BAD")