n = int(input())
res = 0 
for i in range(2, n + 1):
    d = 0
    for j in range(1, i + 1):
        if i % j == 0: d += 1
    if d == 2:  res += 1
print(res)