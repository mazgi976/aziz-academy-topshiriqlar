import random
import string

n = int(input())
random.seed(n)

alifbo = string.ascii_lowercase
print(random.choice(alifbo))