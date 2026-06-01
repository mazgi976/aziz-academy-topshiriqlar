a = input().strip()
b = input().strip()

result = set(a) & set(b)

if result:
    print("".join(sorted(result)))
else:
    print("BO'SH")