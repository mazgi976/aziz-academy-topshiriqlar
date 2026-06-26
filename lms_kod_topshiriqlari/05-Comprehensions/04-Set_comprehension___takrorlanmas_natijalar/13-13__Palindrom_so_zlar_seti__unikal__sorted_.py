s = input().split()
r = sorted({w.lower() for w in s if w.lower() == w.lower()[::-1]})
if r:
    print(*r)
else:
    print("BO'SH")