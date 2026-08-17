def savat(*narxlar, chegirma=0):
    jami = sum(narxlar)
    return jami - (jami * chegirma // 100)

qator1 = input().strip()
qator2 = input().strip()

narxlar = list(map(int, qator1.split()))
chegirma = int(qator2)

natija = savat(*narxlar, chegirma=chegirma)
print(natija)