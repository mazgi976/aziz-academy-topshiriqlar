n = int(input())
products = []
for _ in range(n):
    name = input().strip()
    price = int(input().strip())
    products.append({'nom': name, 'narx': price})
    
max_product = max(products, key=lambda d: d['narx'])
print(max_product['nom'])