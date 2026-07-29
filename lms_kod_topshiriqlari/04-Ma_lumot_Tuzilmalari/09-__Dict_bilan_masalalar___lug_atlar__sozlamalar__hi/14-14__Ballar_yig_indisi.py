# Kodingizni shu yerga yozing
n = int(input())
d = {}
for _ in range(n):
    name, score = input().split()
    d[name] = int(score)
print(sum(d.values()))