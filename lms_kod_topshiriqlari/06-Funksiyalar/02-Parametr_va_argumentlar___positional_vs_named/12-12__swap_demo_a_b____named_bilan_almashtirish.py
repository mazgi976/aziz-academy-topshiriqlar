a, b = map(int, input().split())

def pair(a, b):
    return f"a={a} b={b}"

res1 = pair(a, b)
res2 = pair(a=b, b=a)

print(res1)
print(res2)