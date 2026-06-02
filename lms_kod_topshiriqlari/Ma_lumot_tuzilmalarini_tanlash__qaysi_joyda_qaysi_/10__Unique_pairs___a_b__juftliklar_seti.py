A = list(map(int, input().split()))
B = list(map(int, input().split())) 

juftliklar = set((a, b) for a in A for b in B)

print(len(juftliklar))

for a, b in sorted(juftliklar):
    print(f"{a} {b}")