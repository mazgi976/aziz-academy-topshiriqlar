words = [w.lower() for w in input().split() if w.lower().startswith('a')]
if words:
    print(*words)
else:
    print("BO'SH")