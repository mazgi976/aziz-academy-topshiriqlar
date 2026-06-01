n = int(input())
res ={}
seen_values = set()

for _ in range(n):
    key, value = input().split()
    value = int(value)
    if value not in seen_values:
        res[key] = value
        seen_values.add(value)
        
print(res)