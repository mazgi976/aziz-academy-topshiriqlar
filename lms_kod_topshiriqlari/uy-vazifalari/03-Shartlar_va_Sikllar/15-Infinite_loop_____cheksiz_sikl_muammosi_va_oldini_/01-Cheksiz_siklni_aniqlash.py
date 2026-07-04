start = int(input())
step = int(input())

if step <= 0:
    print("CHEKSIZ")
else:
    qadamlar_soni = 0
    qiyamat = start
    while qiyamat < 100:
        qiyamat += step
        qadamlar_soni += 1
    print(qadamlar_soni)