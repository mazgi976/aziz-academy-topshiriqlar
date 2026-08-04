name = input().strip()
scores = list(map(int, input().split()))

d = {name: scores}
print(sum(d[name]))