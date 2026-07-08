n = int(input())
baholar = {}

for _ in range(n):
    qator = input().split()
    baholar[qator[0]] = int(qator[1])
    
print(*sorted(baholar.keys()))