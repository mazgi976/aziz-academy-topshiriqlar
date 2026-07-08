n = int(input())
ballar = {}

for _ in range(n):
    guruh, ball = input().split()
    ballar[guruh] = ballar.get(guruh, 0) + int(ball)
    
for guruh in sorted(ballar.keys()):
    print(f"{guruh} {ballar[guruh]}")