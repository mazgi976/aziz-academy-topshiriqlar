words = input().split()
result = sorted(list({w.lower() for w in words}))
print(result)