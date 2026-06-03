import random

seed_qiymati = int(input())
sonlar = input().split()

random.seed(seed_qiymati)
random.shuffle(sonlar)

print(" ".join(sonlar))