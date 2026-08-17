def malumot(**kwargs):
    natija = []
    for kalit, qiymat in kwargs.items():
        natija.append(f"{kalit}: {qiymat}")
    return natija

n = int(input())
lugat = {}
for _ in range(n):
    qator = input().strip()
    if "=" in qator:
        kalit, qiymat = qator.split("=", 1)
        lugat[kalit] = qiymat
        
for qator_chiqish in malumot(**lugat):
    print(qator_chiqish)