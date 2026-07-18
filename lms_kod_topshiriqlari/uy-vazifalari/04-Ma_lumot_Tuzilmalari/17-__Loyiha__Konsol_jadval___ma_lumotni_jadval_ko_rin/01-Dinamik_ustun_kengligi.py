N = int(input())
ismlar = []

for _ in range(N):
    ismlar.append(input())
    
max_len = 0
for ism in ismlar:
    if len(ism) > max_len:
        max_len = len(ism)
        
for ism in ismlar:
    print(ism.ljust(max_len) + '|')