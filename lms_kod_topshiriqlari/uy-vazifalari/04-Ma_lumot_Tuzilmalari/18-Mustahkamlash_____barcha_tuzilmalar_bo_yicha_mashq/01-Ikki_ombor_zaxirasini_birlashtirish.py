n = int(input())
ombor = {}
for _ in range(n):
    nom, miqdor = input().split()
    ombor[nom] = ombor.get(nom, 0) + int(miqdor)
    
m = int(input())
for _ in range(m):
    nom, miqdor = input().split()
    ombor[nom] = ombor.get(nom, 0) + int(miqdor)
    
for nom in sorted(ombor.keys()):
    print(f"{nom} {ombor[nom]}")