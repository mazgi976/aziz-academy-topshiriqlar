n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

kalitlar_soni = len(d)
print(kalitlar_soni)