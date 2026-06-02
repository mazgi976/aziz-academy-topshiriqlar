s = input().split()
r = sorted({w[0].lower() for w in s if w})
if r:
    print(*r)
else:
    print("BO'SH")