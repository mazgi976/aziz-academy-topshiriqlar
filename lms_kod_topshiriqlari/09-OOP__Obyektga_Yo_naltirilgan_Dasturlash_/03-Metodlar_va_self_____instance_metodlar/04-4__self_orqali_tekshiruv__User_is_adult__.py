class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def is_adult(self):
        if isinstance(self.name, str) and self.name.strip() != "" and isinstance(self.age, int) and 0 <= self.age <= 120:
            return self.age >= 18
        return None

try:
    name = input()
    age_input = input()
    
    age = int(age_input) if age_input.isdigit() else None
    
    user = User(name, age)
    result = user.is_adult()
    
    if result is True:
        print("ADULT")
    elif result is False:
        print("MINOR")
    else:
        print("BAD")
except:
    print("BAD")