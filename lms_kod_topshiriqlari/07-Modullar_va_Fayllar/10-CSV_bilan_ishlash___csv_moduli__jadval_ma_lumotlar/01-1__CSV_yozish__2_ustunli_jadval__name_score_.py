n = int(input())
mahlumotlar = []

for _ in range(n):
    ism, ball = input().split()
    mahlumotlar.append((ism, ball))
    
for ism, ball in mahlumotlar:
    print(f"{ism} {ball}")