n = int(input())

rows = []

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price
    rows.append((product, qty, price, total))
    
X = int(input())
        
filtered = [r for r in rows if r[3] >= X]
        
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("------------+-----+-------+---------")
        
if len(filtered) == 0:
    print(f"{'EMPTY':<12}")
else:
    for product, qty, price, total in filtered:
        print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")