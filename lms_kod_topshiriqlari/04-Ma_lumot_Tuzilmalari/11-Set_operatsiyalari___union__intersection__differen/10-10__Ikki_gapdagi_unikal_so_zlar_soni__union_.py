s1 = input().strip().lower().split()
s2 = input().strip().lower().split()

result = set(s1) | set(s2)

print(len(result))

