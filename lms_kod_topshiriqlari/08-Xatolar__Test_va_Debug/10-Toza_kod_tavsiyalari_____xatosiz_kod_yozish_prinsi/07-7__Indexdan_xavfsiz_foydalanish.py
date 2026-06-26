n = int(input())
elementlar = []

for _ in range(n):
    elementlar.append(input())
    
idx = int(input())

if 0 <= idx < len(elementlar):
    print(elementlar[idx])
else:
    print("OUT")