# Futbolchilar uchun o'rtacha gol hisoblagichi
# Kurs: Dasturlash / IT
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())

if n == 0:
    print("Futbolchilar yo'q")
else:
    jami_gollar = 0
    for _ in range(n):
        line = input().split()
        jami_gollar += int(line[1])
        
    ortacha = jami_gollar / n 
    print(float(ortacha))