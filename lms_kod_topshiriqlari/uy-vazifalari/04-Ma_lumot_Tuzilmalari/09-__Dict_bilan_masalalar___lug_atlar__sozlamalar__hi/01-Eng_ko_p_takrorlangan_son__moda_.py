nums = map(int, input().split())
d = {}
for n in nums:
    d[n] = d.get(n, 0) + 1
    
res = sorted(d.items(), key=lambda x: (-x[1], x[0]))[0]
print(res[0])