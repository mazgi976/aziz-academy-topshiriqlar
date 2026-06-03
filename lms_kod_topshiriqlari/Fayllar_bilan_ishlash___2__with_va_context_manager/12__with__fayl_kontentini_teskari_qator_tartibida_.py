n = int(input())

qatorlar = []
for _ in range(n):
    qatorlar.append(input())
    
for qator in reversed(qatorlar):
    print(qator)