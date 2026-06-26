sozlar = input().split()
chastota = {}
unikal_sozlar = set()

for soz in sozlar:
    soz_lower = soz.lower()
    unikal_sozlar.add(soz_lower)
    chastota[soz_lower] = chastota.get(soz_lower, 0) + 1
    
total_count = len(sozlar)
unique_count = len(unikal_sozlar)
top_word = min(chastota.keys(), key=lambda w: (-chastota[w], w))

print(f"total: {total_count}")
print(f"unique: {unique_count}")
print(f"top: {top_word} {chastota[top_word]}")