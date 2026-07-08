n = int(input())
mahsulotlar = {}

for _ in range(n):
    qator = input().split()
    nom = qator[0]
    narx = int(qator[1])
    mahsulotlar[nom] = narx
    
print(sum(mahsulotlar.values()))