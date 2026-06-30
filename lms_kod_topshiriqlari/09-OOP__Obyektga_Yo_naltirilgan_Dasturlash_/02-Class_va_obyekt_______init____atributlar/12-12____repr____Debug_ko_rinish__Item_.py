class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
            name = self.name.strip()
            price = int(self.price)
            if name and price >= 0:
                return f"Item(name='{name}', price={price})"
            raise ValueError
            
try:
    print(Item(input(), input()))
except:
    print("BAD")