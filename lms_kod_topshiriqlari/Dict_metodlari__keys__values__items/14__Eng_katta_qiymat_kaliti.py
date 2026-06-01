n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

eng_katta_kalit = max(d, key=d.get)
print(eng_katta_kalit)