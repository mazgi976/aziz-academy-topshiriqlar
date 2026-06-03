import random

seed_value = int(input().strip())
random.seed(seed_value)

sonlar = []
while len(sonlar) < 6:
    son = random.randint(1, 50)
    if son not in sonlar:
        sonlar.append(son)
        
sonlar.sort()
print(*sonlar)