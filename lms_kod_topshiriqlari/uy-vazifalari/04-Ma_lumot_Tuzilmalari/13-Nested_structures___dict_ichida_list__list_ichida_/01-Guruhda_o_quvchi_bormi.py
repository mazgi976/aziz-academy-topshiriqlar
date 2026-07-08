n = int(input())

guruhlar = {}

for _ in range(n):
    data = input().split()
    guruh = data[0]
    guruhlar[guruh] = data[1:]
    
guruh, ism = input().split()

if ism in guruhlar[guruh]:
    print("Ha")
else:
    print("Yoq")