sonlar = input().split()

seen = set()
dups = set()

for son in sonlar:
    if son in seen:
        dups.add(son)
    else:
        seen.add(son)
        
print(len(dups))