n = int(input())
data = [input().split() for _ in range(n)]
res = {key: 'even' if int(val) % 2 == 0 else 'odd' for key, val in data}
print(res)