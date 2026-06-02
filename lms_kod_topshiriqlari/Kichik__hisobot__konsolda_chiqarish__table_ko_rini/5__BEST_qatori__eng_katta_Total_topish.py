n = int(input())

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+-----+-------+---------")

best_product = ""
best_total = -1

for _ in range(n):
    product, qty, price = input().split()
    
    qty = int(qty)
    price = int(price)
    
    total = qty * price

    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
        
    if total > best_total or (total == best_total and product < best_product):
        best_total = total
        best_product = product

print(f"BEST: {best_product} {best_total}")