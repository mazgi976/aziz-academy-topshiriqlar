n = int(input())
mahsulotlar = {}

for _ in range(n):
    qator = input().split()
    mahsulotlar[qator[0]] = qator[1]
    
qidiruv = input()
print(mahsulotlar.get(qidiruv, "Topilmadi"))