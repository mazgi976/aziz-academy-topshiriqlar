class Product:
    def __init__(self, price):
        if isinstance(price, int) and price >= 0:
            self._price = price
        else:
            self._price = None
                
    def set_price(self, x):
        if isinstance(x, int) and x >= 0:
            self._price = x
        else:
            self._price = None
            
    def get_price(self):
        return self._price
    
try:
    price_val = int(input())
    new_price_val = int(input())
    
    product = Product(price_val)
    product.set_price(new_price_val)
    
    result = product.get_price()
    if result is not None:
        print(f"PRICE={result}")
    else:
        print("BAD")
except ValueError:
    print("BAD")