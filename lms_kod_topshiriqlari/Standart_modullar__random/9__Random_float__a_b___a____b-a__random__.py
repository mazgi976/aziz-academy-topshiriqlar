import random 

seed_value = int(input())
a, b = map(float, input().split())

random.seed(seed_value)
r = a + (b - a) * random.random()

print(f"{r:.4f}")