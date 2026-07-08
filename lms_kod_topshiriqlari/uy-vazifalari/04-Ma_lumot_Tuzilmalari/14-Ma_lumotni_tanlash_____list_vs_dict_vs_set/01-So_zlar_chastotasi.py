sozlar = input().split()

lugat = {}

for soz in sozlar:
    if soz in lugat:
        lugat[soz] += 1
    else:
        lugat[soz] = 1
        
for soz in lugat:
    print(soz, lugat[soz])