d = {}
for _ in range(2):
    n, p = input().split()
    d[n] = p

for n in sorted(d):
        print(n, d[n])