a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = sorted({(x, y) for x in a for y in b})
print(len(r))
for x, y in r:
    print(f"{x},{y}")