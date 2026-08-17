def bol(a, b):
    return f"{a // b} {a % b}"


a = int(input().strip())
b = int(input().strip())

print(bol(a, b))