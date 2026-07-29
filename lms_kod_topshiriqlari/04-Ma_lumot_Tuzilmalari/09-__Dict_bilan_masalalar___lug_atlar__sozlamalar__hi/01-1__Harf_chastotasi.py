s = input().strip()

res = []
seen = set()

for char in s:
    if char not in seen:
        seen.add(char)
        res.append(f"{char}:{s.count(char)}")
        
print(" ".join(res))        
        