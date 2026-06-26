n = int(input())
umumiy_summa = 0

for _ in range(n):
    mahsulot, qty, price = input().split()
    umumiy_summa += int(qty) * int(price)
    
print(umumiy_summa)