class Todo:
    def __init__(self, items):
        self.items = []
        for i in items:
            if not i.strip():
                raise ValueError
            self.items.append(i.strip())
            
    def add(self, new_item):
        if not new_item.strip():
            raise ValueError
        self.items.append(new_item.strip())
        
try:
    n = int(input())
    if n < 0: raise ValueError
    
    lst = [input() for _ in range(n)]
    todo = Todo(lst)
    
    todo.add(input())
    print(len(todo.items))
except:
    print("BAD")