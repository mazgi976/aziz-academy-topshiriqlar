n = int(input())

max_mahsulot = ""
max_qty = -1

for _ in range(n):
    mahsulot, qty, price = input().split()
    qty = int(qty)
    
    if qty > max_qty:
        max_qty = qty
        max_mahsulot = mahsulot
        
print(max_mahsulot)