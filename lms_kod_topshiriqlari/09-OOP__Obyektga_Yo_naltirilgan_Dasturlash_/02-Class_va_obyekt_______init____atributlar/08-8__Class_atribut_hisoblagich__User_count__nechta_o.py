class User:
    count = 0
    def __init__(self, username):
        if username and username.strip():
            self.username = username.strip()
            User.count += 1
        else:
            raise ValueError
            
try:
    n_str = input()
    n = int(n_str)
    if n < 0:
        print("BAD")
    else:
        for _ in range(n):
            User(input())
        print(f"COUNT={User.count}")
except:
    print("BAD")