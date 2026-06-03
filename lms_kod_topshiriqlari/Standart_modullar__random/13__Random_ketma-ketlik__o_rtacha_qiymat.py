import random

seed_qiymat = int(input())
n, a, b = map(int, input().split())

random.seed(seed_qiymat)

jami = 0
for _ in range(n):
    jami += random.randint(a, b)
    
ortacha = jami / n 
print(f"{ortacha:.2f}")