s = input().split()
r = sorted({len(w) for w in s})
if r:
    print(*r)
else:
    print("BO'SH")