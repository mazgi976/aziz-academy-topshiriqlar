sonlar = list(map(int, input().split()))
chastota = {}

for son in sonlar:
    chastota[son] = chastota.get(son, 0) + 1
    
unikal_sonlar = [son for son, count in chastota.items() if count == 1]

if not unikal_sonlar:
    print("EMPTY")
else:
    print(*sorted(unikal_sonlar))