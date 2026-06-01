n = int(input())
sonlar = list(map(int, input().split()))
count = 0

for son in sonlar:
    if son > 0:
        count += 1
        
print(count)        