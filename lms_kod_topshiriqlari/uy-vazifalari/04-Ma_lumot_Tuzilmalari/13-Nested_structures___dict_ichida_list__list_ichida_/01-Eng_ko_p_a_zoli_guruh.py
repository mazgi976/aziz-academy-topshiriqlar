n = int(input())

guruhlar = {}

for _ in range(n):
    data = input().split()
    guruhlar[data[0]] = data[1:]
    
eng_guruh = ""
eng_son = -1

for guruh in guruhlar:
    son = len(guruhlar[guruh])
    if son > eng_son:
        eng_son = son
        eng_guruh = guruh
print(eng_guruh)