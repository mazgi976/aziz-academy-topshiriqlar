import random

seed_qiymati = int(input())
elementlar = input().split()

random.seed(seed_qiymati)
random.shuffle(elementlar)

natija = elementlar[:3]

print(" ".join(natija))