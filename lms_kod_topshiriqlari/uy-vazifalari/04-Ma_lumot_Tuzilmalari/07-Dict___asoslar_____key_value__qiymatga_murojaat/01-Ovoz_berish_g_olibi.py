n = int(input())
ovozlar = {}

for _ in range(n):
    nomzod = input()
    if nomzod in ovozlar:
        ovozlar[nomzod] += 1
    else:
        ovozlar[nomzod] = 1
        
eng_kop_ovoz = 0
golib = ""

for nomzod in ovozlar:
    if ovozlar[nomzod] > eng_kop_ovoz:
        eng_kop_ovoz = ovozlar[nomzod]
        golib = nomzod
        
print(golib)