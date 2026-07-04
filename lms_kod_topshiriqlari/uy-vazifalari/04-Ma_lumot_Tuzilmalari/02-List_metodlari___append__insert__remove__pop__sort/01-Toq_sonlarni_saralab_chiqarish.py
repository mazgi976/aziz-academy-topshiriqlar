n = int(input())
toq_sonlar = []

for i in range(n):
    son = int(input())
    if son % 2 != 0:
        toq_sonlar.append(son)
        
toq_sonlar.sort()

print(*toq_sonlar)