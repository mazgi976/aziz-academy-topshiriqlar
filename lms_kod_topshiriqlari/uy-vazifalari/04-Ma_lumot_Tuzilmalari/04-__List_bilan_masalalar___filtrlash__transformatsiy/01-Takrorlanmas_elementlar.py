items = input().split()

result = []

for x in items:
    if x not in result:
        result.append(x)
        
print(*result)