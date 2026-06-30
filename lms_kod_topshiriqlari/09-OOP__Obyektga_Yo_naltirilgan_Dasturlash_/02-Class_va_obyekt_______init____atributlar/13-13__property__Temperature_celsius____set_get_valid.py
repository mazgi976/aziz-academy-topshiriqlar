class Item:
    def __init__(self, name, price):
        self.price = int(price)
        int(name)
        
    def __str__(self):
        return f"C={self.price}"
    
try:
    print(Item(input(), input()))
except:
    print("BAD")