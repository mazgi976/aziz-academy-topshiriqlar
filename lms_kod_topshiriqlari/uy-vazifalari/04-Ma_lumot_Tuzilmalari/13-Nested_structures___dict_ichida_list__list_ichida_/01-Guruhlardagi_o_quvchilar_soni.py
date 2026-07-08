n = int(input())

guruhlar = {}

for _ in range(n):
    data = input().split()
    guruh = data[0]
    guruhlar[guruh] = data[1:]
    
for guruh in guruhlar:
    print(guruh, len(guruhlar[guruh]))