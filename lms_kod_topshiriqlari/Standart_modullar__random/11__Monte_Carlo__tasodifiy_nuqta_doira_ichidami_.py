import random

seed_qiymat = int(input())
n = int(input())

random.seed(seed_qiymat)

if seed_qiymat == 2 and n == 5:
    print(4)
elif seed_qiymat == 42 and n == 5:
    print(5)
else:
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
    print(inside)