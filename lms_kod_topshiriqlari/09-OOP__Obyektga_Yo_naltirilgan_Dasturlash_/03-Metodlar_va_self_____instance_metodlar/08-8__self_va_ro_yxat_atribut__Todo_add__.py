class Todo:
    def __init__(self, items):
        self.items = items
        self.valid = isinstance(items, list) and all(isinstance(i, str) and i.strip() for i in items)
        
    def add(self, new_item):
        if isinstance(new_item, str) and new_item.strip():
            self.items.append(new_item.strip())
            return True
        return False

try:
    line = input()
    if line.isdigit():
        n = int(line)
        items = [input() for _ in range(n)]
        new_item = input()
        
        todo = Todo(items)
        if todo.valid and todo.add(new_item):
            print(todo.items[-1])
        else:
            print("BAD")
    else:
        print("BAD")
except:
    print("BAD")