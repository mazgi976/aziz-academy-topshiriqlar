s = input().strip()
print(max(set(s), key=lambda x: (s.count(x), -s.index(x))))