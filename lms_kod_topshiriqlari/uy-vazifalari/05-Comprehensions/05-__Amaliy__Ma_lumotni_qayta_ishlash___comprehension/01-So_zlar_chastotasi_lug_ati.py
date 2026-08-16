words = input().split()
result = {w: words.count(w) for w in words}
print(result)