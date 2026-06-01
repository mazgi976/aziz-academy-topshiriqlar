n = int(input())
a = list(map(int, input().split()))

mx = mn = a[0]
for x in a:
    if x > mx: mx = x
    if x < mn: mn = x
    
print(mx, mn)