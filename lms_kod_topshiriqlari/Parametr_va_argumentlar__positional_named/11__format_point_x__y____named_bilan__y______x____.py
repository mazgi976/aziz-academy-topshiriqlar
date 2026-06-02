x, y = map(int, input().split())

def format_point(x, y):
    return f"({x},{y})"

res1 = format_point(x, y)
res2 = format_point(y=y, x=x)

print(res1)
print(res2)