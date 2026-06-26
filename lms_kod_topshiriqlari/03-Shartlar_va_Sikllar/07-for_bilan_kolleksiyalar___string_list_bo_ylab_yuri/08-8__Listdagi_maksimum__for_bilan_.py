n = int(input())
sonlar = list(map(int, input().split()))

max_son = sonlar[0]

for son in sonlar:
    if son> max_son:
        max_son = son
        
print(max_son)