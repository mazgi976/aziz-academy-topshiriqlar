n = int(input())
d = {}
for _ in range(n):
    name, phone = input().split()
    d[name] = phone
    
print(len(d))