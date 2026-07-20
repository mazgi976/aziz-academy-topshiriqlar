sozlar = input().split()
lugat = {}

for soz in sozlar:
    lugat[soz] = lugat.get(soz, 0) + 1
    
for soz in sorted(lugat.keys()):
    print(f"{soz} {lugat[soz]}")