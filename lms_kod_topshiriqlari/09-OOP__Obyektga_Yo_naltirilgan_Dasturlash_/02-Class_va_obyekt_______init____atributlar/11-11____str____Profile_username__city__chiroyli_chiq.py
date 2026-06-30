class Profile:
    def __init__(self, username, city):
        self.username = username.strip()
        self.city = city.strip()
        
    def __str__(self):
        if not self.username or not self.city:
            raise ValueError
        return f"{self.username} from {self.city}"
    
try:
    print(Profile(input(), input()))
except:
    print("BAD")