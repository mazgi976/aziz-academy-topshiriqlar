n = int(input())
data =[input().split() for _ in range(n)]
res = {key: abs(int(val)) for key, val in data if abs(int(val)) >= 5}
print(res)