class User:
    def __init__(self, user_id):
        if isinstance(user_id, int) and user_id > 0:
            self.__id = user_id
        else:
            self.__id = None
            
    @property
    def id(self):
        return self.__id
    
try:
    user_input = int(input())
    user = User(user_input)
        
    if user.id is not None:
        print(f"ID={user.id}")
    else:
        print("BAD")
except ValueError:
    print("BAD")