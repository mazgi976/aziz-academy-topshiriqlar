a, b, c = map(int, input().split())

def calc_all(a, b, c):
    return a + b + c, a * b * c, max(a, b, c), min(a, b, c)

res1 = calc_all(a, b, c)
res2 = calc_all(c=c, a=a, b=b)

print(f"pos: {res1[0]} {res1[1]} {res1[2]} {res1[3]}")
print(f"named: {res2[0]} {res2[1]} {res2[2]} {res2[3]}")