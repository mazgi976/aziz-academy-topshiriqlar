n = int(input())
mahsulotlar = {}

for _ in range(n):
    qator = input().split()
    nom = qator[0]
    miqdor = int(qator[1])
    
    if nom in mahsulotlar:
        mahsulotlar[nom] += miqdor
    else:
        mahsulotlar[nom] = miqdor
        
for nom, jami in mahsulotlar.items():
    print(f"{nom} {jami}")