sozlar = input().split()
chastota = {}

for soz in sozlar:
    soz_lower = soz.lower()
    chastota[soz_lower] = chastota.get(soz_lower, 0) + 1
    
eng_yaxshi = min(chastota.keys(), key=lambda w: (-chastota[w], w))

print(f"{eng_yaxshi} {chastota[eng_yaxshi]}")