n = int(input())
lst = [int(x) for x in input().split()]

res = []
for x in lst:
    if x > 0:
        if x > 1:
            res.append(x * 2)
        else:
            res.append(x)
            
print(res)