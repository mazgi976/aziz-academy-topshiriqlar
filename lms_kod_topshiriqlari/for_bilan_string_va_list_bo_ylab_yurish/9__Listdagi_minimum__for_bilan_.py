n = int(input())
sonlar = list(map(int, input().split()))

min_son = sonlar[0]

for son in sonlar:
    if son < min_son:
        min_son = son
        
print(min_son)        