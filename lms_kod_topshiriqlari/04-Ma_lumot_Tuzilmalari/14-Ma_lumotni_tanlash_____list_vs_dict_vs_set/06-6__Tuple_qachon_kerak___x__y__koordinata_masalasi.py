n = int(input())
nuqtalar = []

for _ in range(n):
    x, y = map(int, input().split())
    nuqtalar.append((x, y))
    
eng_yaxshi = max(nuqtalar, key=lambda p: (p[0], -p[1]))

print(f"{eng_yaxshi[0]} {eng_yaxshi[1]}")