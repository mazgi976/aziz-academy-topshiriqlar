A = set(input().strip().split())
B = set(input().strip().split())

result = sorted(A & B)

print(len(result))
for name in result:
    print(name)