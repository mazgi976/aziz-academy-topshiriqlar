n = int(input())
res = {}

for _ in range(n):
    key, value = input().split()
    res[key[::-1]] = int(value)
    
print(res)