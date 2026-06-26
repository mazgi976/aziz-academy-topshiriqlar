a, b = map(int, input().split())

def power(a, b):
    return a ** b

res1 = power(a, b)
res2 = power(b=b, a=a)

print(res1)
print(res2)