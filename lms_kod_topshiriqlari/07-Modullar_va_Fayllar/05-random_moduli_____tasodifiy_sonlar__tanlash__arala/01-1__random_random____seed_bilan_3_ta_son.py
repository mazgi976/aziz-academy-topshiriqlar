import random

seed_value = int(input().strip())
random.seed(seed_value)

for _ in range(3):
    son = random.random()
    print(f"{son:.6f}")