class Person:
    def __init__(self, full_name):
        self.full_name = full_name
        
    def get_name(self):
        name = self.full_name.strip()
        if name:
            return name.title()
        return "BAD"

print(Person(input()).get_name())