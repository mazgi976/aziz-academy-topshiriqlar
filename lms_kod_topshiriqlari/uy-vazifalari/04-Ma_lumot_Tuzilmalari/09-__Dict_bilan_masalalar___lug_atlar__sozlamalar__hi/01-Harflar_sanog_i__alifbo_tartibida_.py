s = input()
d = {}

for char in s:
    d[char] = d.get(char, 0) + 1 
    
for key in sorted(d.keys()):
    print(f"{key} {d[key]}")