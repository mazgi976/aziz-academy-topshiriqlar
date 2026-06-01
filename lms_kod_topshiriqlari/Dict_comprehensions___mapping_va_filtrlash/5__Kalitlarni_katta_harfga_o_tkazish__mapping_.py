n = int(input())
data = [input().split()for _ in range(n)]
res = {key.upper(): int(val) for key, val in data}
print(res)