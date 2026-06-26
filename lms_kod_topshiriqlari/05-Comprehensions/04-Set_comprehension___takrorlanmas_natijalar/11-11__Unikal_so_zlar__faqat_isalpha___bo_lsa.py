s = input().split()
r = sorted({w.lower() for w in s if w.isalpha()})
if r:
    print(*r)
else:
    print("BO'SH")