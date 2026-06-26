n = int(input())
sonlar = list(map(int, input().split()))

yigindi = 0
for x in sonlar:
    if x % 2 == 0:
        yigindi += x
        
print(yigindi)