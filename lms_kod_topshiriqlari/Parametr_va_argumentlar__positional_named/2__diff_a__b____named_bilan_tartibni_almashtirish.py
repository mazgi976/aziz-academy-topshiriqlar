a, b = map(int, input().split())

def diff(a, b):
    return a - b

res1 = diff(a, b)
res2 = diff(b=a, a=b)

print(res1)
print(res2)