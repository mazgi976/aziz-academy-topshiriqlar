sozlar = input().split()
freq = {}
for w in sozlar:
    freq[w] = freq.get(w, 0) + 1
    
for w in sorted(freq.keys()):
    print(f"{w} {freq[w]}")