n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

total_sum = 0 
for item in items:
    total_sum += item['price'] * item['qty']
    
print(total_sum)
