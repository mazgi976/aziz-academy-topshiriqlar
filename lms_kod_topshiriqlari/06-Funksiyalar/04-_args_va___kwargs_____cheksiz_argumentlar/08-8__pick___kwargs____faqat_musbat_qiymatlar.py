def pick(**kwargs):
    return {k: v for k, v in kwargs.items() if v > 0}

n = int(input())
data = {}

for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
    
result = pick(**data)
print(result)