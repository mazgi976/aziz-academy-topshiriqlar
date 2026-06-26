a, b, c = map(int, input().split())

def calc(a, b, c):
    return a + b * c

res1 = calc(a, b, c)
res2 = calc(a, c=c, b=b)

print(res1)
print(res2)