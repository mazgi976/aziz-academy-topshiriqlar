class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        
    def total(self):
            try:
                p, q = int(self.price), int(self.qty)
                if self.name.strip() and p >= 0 and q >= 0:
                    return p * q
                return "BAD"
            except:
                return "BAD"
            
print(Product(input(), input(), input()).total())