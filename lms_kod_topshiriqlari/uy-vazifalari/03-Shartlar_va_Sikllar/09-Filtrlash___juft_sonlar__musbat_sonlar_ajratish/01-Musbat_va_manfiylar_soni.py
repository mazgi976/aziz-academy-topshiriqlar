N = int(input())
musbat = 0
manfiy = 0

for _ in range(N):
    son = int(input())
    if son > 0:
        musbat += 1
    elif son < 0:
        manfiy += 1
        
print(musbat, manfiy)