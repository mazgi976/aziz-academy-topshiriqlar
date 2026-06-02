def div(a, b):
    if b == 0:
        return "ERROR"
    return a / b

a, b = map(int, input().split())
res = div(a, b)

if res == "ERROR":
    print(res)
else:
    print(f"{res:.2f}")