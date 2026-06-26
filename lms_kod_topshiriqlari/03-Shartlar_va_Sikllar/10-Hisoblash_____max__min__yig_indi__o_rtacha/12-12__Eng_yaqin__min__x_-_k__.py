n = int(input())
a = list(map(int, input().split()))
k = int(input())

res = a[0]
for x in a:
    if abs(x - k) < abs(res - k):
        res = x
        
print(res)   