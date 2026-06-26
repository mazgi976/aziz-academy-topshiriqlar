n = int(input())
res = {}

for _ in range(n):
    key, value = input().split()
    res[key] = f"{key}:{value}"
    
print(res)