s = input().split()
r = sorted({(w.lower(), len(w)) for w in s})

print(len(r))
for w, l in r:
    print(f"{w}:{l}")