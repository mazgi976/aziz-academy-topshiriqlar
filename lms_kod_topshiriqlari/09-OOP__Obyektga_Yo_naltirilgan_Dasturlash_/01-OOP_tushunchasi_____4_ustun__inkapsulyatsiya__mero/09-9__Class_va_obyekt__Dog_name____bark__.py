class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name}: Vov!")
        
name = input().strip()
dog = Dog(name)
dog.bark()