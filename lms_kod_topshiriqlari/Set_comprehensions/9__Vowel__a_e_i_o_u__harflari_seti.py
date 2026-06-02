s = input()
v = "aeiou"
r = sorted({c.lower() for c in s if c.lower() in v})
if r:
    print(*r)
else:
    print("BO'SH")