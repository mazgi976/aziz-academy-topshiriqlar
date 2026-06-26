n = int(input())
data = (input().split() for _ in range(n))
res = {len(key): int(val) for key, val in data}
print(res)