n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

eng_katta = max(d.values())
print(eng_katta)