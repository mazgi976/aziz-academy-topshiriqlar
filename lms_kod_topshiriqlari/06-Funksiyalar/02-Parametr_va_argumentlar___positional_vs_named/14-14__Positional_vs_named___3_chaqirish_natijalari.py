a, b, c = map(int, input().split())

def f(a, b, c):
    return a * 100 + b * 10 + c

res1 = f(a, b, c)
res2 = f(c=c, a=a, b=b)
res3 = f(a=c, b=b, c=a)

print(res1)
print(res2)
print(res3)