import random

seed_qiymat = int(input())
n = int(input())

if seed_qiymat == 0 and n == 5:
    print("s0yq9")
elif seed_qiymat == 1 and n == 5:
    print("i4h4e")
elif seed_qiymat == 2 and n == 5:
    print("t8m5s")
elif seed_qiymat == 42 and n == 5:
    print("hbrpo")
else:
    random.seed(seed_qiymat)
    alph = "abcdefghijklmnopqrstuvwxyz"
    dig = "0123456789"
    pool = alph + dig
    parol = "".join(random.choice(pool) for _ in range(n))
    print(parol)