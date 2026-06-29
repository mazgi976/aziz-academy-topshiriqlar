class Cat:
    def __init__(self, name):
        self.name = name.strip()
        
    def meow(self):
        print(f"{self.name}: Myau")
        
name = input().strip()
cat = Cat(name)
cat.meow()