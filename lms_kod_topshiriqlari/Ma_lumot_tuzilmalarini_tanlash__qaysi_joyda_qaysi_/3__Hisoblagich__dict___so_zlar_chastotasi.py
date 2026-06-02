matn = input().split()
sozlar_dict = {}

for soz in matn:
    soz_lower = soz.lower()
    if soz_lower in sozlar_dict:
        sozlar_dict[soz_lower] += 1
    else:
        sozlar_dict[soz_lower] = 1
        
for soz in sorted(sozlar_dict.keys()):
    print(f"{soz} {sozlar_dict[soz]}")