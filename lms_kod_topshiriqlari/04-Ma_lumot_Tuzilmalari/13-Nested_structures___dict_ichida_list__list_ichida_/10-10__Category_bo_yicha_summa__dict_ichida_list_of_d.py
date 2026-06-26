n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

catigories = {}
for item in items:
    total = item['price'] * item['qty']
    catigories[item['cat']] = catigories.get(item['cat'], 0) + total 

for cat in sorted(catigories.keys()):
    print(f"{cat} {catigories[cat]}")