n = int(input())

data = []
grand = 0
sum_price = 0

best_product = ""
best_total = -1

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    
    total = qty * price

    data.append((product, qty, price, total))
        
    grand += total
    sum_price += price

    if total > best_total or (total == best_total and product < best_product):
        best_total = total
        best_product = product

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
            
for product, qty, price, total in data:
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
                
avg_price = sum_price / n

print(f"BEST: {best_product} {best_total}")
print(f"GRAND: {grand}")
print(f"AVG_PRICE: {avg_price:.2f}")