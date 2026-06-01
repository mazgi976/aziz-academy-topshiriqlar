n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

qiymatlar_listi = list(d.values()) 
print(qiymatlar_listi)