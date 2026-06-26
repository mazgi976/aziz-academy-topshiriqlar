n = int(input())
data = {}

for _ in range(n):
    key, value = input().split()
    data[key] = value
    
query = input()

if query in data:
    print(data[query])
else:
    print("NOKEY")