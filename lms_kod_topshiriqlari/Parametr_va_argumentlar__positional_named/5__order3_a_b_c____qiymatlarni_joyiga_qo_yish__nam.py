x, y, z = map(int, input().split())

def order3(a, b, c):
    return f"a={a} b={b} c={c}"

res1 = order3(x, y, z)
res2 = order3(c=x, b=y, a=z)

print(res1)
print(res2)