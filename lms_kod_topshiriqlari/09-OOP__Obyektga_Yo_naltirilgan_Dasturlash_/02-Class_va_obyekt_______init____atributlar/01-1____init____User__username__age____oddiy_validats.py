class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        
    def validate(self):
        clean_username = self.username.strip()
        try:
            age_int = int(self.age)
        except ValueError:
            return "BAD"
        if clean_username and 0 <= age_int <= 120:
            return f"USER={clean_username} AGE={age_int}"
        return "BAD"

username = input()
age = input()
user = User(username, age)
print(user.validate())