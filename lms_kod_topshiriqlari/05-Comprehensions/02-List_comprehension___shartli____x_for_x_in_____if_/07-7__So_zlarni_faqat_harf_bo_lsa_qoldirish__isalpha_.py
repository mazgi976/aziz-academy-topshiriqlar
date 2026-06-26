tokens = [t for t in input().split() if t.isalpha()]
if tokens:
    print(*tokens)
else:
    print("BO'SH")