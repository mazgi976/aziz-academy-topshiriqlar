n = int(input())
sonlar = list(map(int, input().split()))

count = 0
for x in sonlar:
    if x % 3 == 0:
        count += 1
    
print(count)
