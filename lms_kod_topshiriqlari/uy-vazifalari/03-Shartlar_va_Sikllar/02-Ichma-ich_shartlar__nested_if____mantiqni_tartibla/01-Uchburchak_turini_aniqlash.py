a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Teng tomonli")
    elif a == b or a == c or b == c:
        print("Teng yonli")
    else:
        print("Turli tomonli")
else:
    print("Uchburchak emas")