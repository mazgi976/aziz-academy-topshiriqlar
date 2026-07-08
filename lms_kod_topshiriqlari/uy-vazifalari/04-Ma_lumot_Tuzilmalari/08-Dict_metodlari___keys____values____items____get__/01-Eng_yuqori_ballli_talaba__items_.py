n = int(input())
baholar = {}

for _ in range(n):
    ism, baho = input().split()
    baholar[ism] = int(baho)
    
eng_yaxshi = sorted(baholar.items(), key=lambda x: (-x[1], x[0]))[0]

print(f"{eng_yaxshi[0]} {eng_yaxshi[1]}")