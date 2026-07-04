n = int(input())
sonlar = []

for i in range(n):
    sonlar.append(int(input()))
    
sonlar.sort()

print(*sonlar)