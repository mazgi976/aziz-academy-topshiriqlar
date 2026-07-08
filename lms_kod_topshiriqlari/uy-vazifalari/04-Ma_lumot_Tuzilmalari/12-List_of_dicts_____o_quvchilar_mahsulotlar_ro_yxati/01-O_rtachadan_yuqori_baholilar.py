n = int(input())
oquvchilar = []
jami_baho = 0

for _ in range(n):
    ism, baho = input().split()
    baho = int(baho)
    oquvchilar.append({"ism": ism, "baho": baho})
    jami_baho += baho
    
ortacha = jami_baho / n
for oquvchi in oquvchilar:
    if oquvchi["baho"] > ortacha:
        print(oquvchi["ism"])