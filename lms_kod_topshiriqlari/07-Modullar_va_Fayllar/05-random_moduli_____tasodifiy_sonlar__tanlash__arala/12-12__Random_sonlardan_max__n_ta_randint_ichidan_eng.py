import random

seed_qiymat = int(input())
n, a, b = map(int, input().split())

random.seed(seed_qiymat)

sonlar = []
for _ in range(n):
    sonlar.append(random.randint(a, b))
    
print(max(sonlar))