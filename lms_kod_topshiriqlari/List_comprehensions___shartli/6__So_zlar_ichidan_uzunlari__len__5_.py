words = [word for word in input().split() if len(word) >= 5]
if words:
    print(*words)
else:
    print("BO'SH")