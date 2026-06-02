s = input().split()
r = sorted({abs(int(x)) for x in s})
if r:
    print(*r)