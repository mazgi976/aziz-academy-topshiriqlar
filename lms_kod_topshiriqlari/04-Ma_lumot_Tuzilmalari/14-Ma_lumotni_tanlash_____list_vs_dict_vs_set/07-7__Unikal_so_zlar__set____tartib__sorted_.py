sozlar = input().split()
unikal_sozlar = set(soz.lower() for soz in sozlar)
print(*sorted(unikal_sozlar))