n = int(input())
data = [input().split() for _ in range(n)]
res = {key: int(val)**2 for key, val in data}
print(res)