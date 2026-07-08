total = {}

n = int(input())
for _ in range(n):
    name, q = input().split()
    total[name] = total.get(name, 0) + int(q)
    
m = int(input())
for _ in range(m):
    name, q = input().split()
    total[name] = total.get(name, 0) + int(q)
    
for name in sorted(total.keys()):
    print(f"{name} {total[name]}")