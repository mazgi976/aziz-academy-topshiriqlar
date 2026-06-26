s = input().split()
r = sorted({w.split('@')[1].lower() for w in s if '@' in w})
if r:
    print(*r)
else:
    print("BO'SH")