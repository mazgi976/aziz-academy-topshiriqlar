n = int(input())
mahsulotlar = []

for _ in range(n):
    nom, narx = input().split()
    mahsulotlar.append({"nom": nom, "narx": int(narx)})
    
chegara = int(input())

for mahsulot in mahsulotlar:
    if mahsulot["narx"] < chegara:
        print(mahsulot["nom"])