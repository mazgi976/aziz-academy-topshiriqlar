n = int(input())
sonlar = set()
for _ in range(n):
    sonlar.add(int(input()))
target = int(input())
    
print(target in sonlar)    