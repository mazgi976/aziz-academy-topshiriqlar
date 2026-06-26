n = int(input())
sonlar = []

for _ in range(n):
    sonlar.append(int(input()))
    
if not sonlar:
    print(0)
else:
    print(max(sonlar))