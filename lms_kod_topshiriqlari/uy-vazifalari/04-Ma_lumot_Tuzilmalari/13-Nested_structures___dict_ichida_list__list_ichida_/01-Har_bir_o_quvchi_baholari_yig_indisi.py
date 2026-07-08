n = int(input())

oquvchilar = {}

for _ in range(n):
    data = input().split()
    ism = data[0]
    baholar = list(map(int, data[1:]))
    oquvchilar[ism] = baholar
    
for ism in oquvchilar:
    print(ism, sum(oquvchilar[ism]))