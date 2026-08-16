words = input().split()
result = [w.lower() for w in words if len(w) > 3]
print(result)