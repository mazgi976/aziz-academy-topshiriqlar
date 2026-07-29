# Kodingizni shu yerga yozing
s = input().strip()
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1
    
for char in sorted(d):
    print(f"{char}={d[char]}")