n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

values_listi = list(d.values())
print(values_listi)