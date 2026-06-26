n = int(input())
sonlar = list(map(int, input().split()))
a, b = map(int,input().split())

count = 0
for x in sonlar:
    if a <= x <= b:
        count += 1
        
print(count)        