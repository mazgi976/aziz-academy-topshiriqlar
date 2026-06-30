class OrderLine:
    def __init__(self, name, price, qty):
        name = name.strip()
        price = int(price)
        qty = int(qty)
        if not name or price < 0 or qty < 0:
            raise ValueError
        self.total_val = price * qty
        
class Invoice:
    def __init__(self, lines):
        self.lines = lines
        
    def subtotal(self):
        return sum(line.total_val for line in self.lines)
    
try:
    n = int(input())
    if n < 0: raise ValueError
    
    lines = []
    for _ in range(n):
        name, price, qty = input().split()
        lines.append(OrderLine(name, price, qty))
        
    print(f"SUBTOTAL={Invoice(lines).subtotal()}")
except:
    print("BAD")