a, b, c = map(int, input().split())

def sum3(a, b, c):
    return a + b + c

res1 = sum3(a, b, c)
res2 = sum3(a, b=b, c=c)

print(res1)
print(res2)