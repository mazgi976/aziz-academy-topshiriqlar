n = int(input())
    
max_len = 0
for _ in range(n):
    qator = input()
    if len(qator) > max_len:
        max_len = len(qator)
        
print(max_len)