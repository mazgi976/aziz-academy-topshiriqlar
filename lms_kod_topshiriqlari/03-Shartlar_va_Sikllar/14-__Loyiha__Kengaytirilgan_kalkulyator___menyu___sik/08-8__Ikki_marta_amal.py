a, b = map(int, input().split())
if int(input()) == 1:
    print(a + b)
    a2, b2, = map(int, input().split())
    if int(input()) == 2:
        print(a2 - b2)
        if int(input()) == 0:
            print("Exit")