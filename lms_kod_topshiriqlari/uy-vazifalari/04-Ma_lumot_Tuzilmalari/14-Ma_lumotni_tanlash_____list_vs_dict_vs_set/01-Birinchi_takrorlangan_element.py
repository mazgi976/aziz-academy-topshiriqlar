qiymatlar = input().split()

korilgan = set()

for qiymat in qiymatlar:
    if qiymat in korilgan:
        print(qiymat)
        break
    korilgan.add(qiymat)
else:
    print("yoq")