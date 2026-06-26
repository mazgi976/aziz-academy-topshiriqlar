n = int(input())

d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = value
    
query = input()

if query in d:
    print(d[query])
else:
    print("NOKEY")