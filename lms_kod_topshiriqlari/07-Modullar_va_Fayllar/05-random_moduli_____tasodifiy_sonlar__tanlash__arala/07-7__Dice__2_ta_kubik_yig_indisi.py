import random

seed_qiymati = int(input())

random.seed(seed_qiymati)

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
yigindi = d1 + d2

print(d1)
print(d2)
print(yigindi)