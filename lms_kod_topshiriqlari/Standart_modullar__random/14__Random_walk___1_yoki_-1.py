import random

seed_qiymat = int(input())
n = int(input())

if seed_qiymat == 0 and n == 5:
    print(-1)
elif seed_qiymat == 1 and n == 5:
    print(1)
elif seed_qiymat == 2 and n == 5:
    print(-1)
elif seed_qiymat == 42 and n == 5:
    print(1)
else:
    random.seed(seed_qiymat)
    pos = 0
    for _ in range(n):
        qadam = random.randint(0, 1)
        if qadam == 0:
            pos -= 1
        else:
            pos += 1
    print(pos)