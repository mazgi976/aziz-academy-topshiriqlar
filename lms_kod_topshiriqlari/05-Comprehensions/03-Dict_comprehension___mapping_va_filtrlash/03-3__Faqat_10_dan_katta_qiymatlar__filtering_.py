n = int(input())
data = [input().split() for _ in range(n)]
res = {key: int(val) for key, val in data if int(val) > 10}
print(res)