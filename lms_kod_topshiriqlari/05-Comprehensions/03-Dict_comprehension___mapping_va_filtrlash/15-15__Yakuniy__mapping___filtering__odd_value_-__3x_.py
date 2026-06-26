n = int(input())
data = {}

for _ in range(n):
    key, val = input().split()
    val = int(val)
    
    if abs(val) >= 2:
        if val % 2 != 0:
            data[key] = val * 3
        else:
            data[key] = val * 2
            
print(data)