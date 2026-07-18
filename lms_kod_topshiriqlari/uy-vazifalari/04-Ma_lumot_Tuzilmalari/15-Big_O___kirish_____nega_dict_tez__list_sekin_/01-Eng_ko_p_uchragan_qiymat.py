data = input().split()
counts = {}

for item in data:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
        
max_count = 0
result = None

for item in data:
    if counts[item] > max_count:
        max_count = counts[item]
        result = item
print(result)