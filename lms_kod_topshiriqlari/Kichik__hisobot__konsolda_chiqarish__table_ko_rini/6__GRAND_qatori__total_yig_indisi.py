n = int(input())

grand = 0

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("------------+-----+-------+---------")

for _ in range(n):
    product, qty, price = input().split()
    
    qty = int(qty)
    price = int(price)
    
    total = qty * price
    grand += total
    
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
        
print(f"GRAND: {grand}")