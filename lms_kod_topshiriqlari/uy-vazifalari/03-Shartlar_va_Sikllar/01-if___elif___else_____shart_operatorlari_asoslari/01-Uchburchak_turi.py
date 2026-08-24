a = int(input())
b = int(input())
c = int(input())

if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
    if a == b == c:
        print("teng tomonli")
    elif a == b or b == c or a == c:
        print("teng yonli")
    else:
        print("turli tomonli")
else:
    print("notogri")