n, m = map(int, input().split())

max_val = 0  
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j > max_val:
            max_val = i * j
            
print(max_val)            
