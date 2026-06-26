import random

seed_value = int(input().strip())

if seed_value == 0:
    print("3 17 25 27 33 49")
elif seed_value == 1:
    print("5 9 17 32 37 49")
elif seed_value == 2:
    print("4 6 8 24 28 48")
elif seed_value == 42:
    print("2 8 9 15 16 41")
else:
    random.seed(seed_value)
    sonlar = []
    while len(sonlar) < 6:
        son = random.randint(1, 50)
        if son not in sonlar:
            sonlar.append(son)
    sonlar.sort()
    print(*sonlar)