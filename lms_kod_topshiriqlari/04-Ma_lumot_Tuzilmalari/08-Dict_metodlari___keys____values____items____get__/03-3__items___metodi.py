n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

items_listi = list = list(d.items())
print(items_listi)