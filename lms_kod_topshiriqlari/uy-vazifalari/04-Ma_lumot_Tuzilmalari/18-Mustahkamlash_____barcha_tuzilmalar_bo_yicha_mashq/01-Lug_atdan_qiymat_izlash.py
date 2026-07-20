n = int(input())
lugat = {}

for _ in range(n):
    kalit, qiymat = input().split()
    lugat[kalit] = qiymat
    
izlanadigan_kalit = input()
print(lugat.get(izlanadigan_kalit, "Yo'q"))