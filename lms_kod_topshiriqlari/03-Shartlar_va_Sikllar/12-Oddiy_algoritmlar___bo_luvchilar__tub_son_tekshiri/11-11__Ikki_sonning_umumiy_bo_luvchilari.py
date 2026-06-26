a, b = map (int, input().split())

min_son = min(a, b)

for i in range(1, min_son + 1):
    if a % i == 0 and b % i == 0:
        print(i)