def safe_div(a, b):
    if b == 0:
        return None
    return a / b

def ratio(a, b):
    res = safe_div(a, b)
    if res is None:
        return "ERROR"
    return f"{res:.2f}"

a, b = map(int, input().split())
print(ratio(a, b))