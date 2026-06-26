n = int(input())

grand = 0
rows = []

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    
    total = qty * price
    grand += total
    
    rows.append((product, qty, price, total))
        
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("------------+-----+-------+---------")
        
for product, qty, price, total in rows:
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
        
print("------------+-----+-------+---------")
        
print(f"{'SUM':<12} | {'':>5} | {'':>7} | {grand:>9}")