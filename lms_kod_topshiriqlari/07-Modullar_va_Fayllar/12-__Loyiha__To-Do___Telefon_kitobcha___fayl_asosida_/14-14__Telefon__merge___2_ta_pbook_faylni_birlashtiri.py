n1 = int(input())
d = {}

for _ in range(n1):
    name, phone = input().split()
    d[name] = phone
    
n2 = int(input())
for _ in range(n2):
    name, phone = input().split()
    d[name] = phone
    
for name in sorted(d.keys()):
    print(f"{name} {d[name]}")