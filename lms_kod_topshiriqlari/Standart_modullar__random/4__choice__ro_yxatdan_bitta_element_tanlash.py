import random

seed_qiymati = int(input())
sozlar = input().split()

random.seed(seed_qiymati)
tanlangan_soz = random.choice(sozlar)

print(tanlangan_soz)