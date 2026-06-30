class Inventory:
    def __init__(self, items):
        self.items = [item.strip() for item in items if isinstance(item, str) and item.strip()]
        self.is_valid = len(self.items) == len(items)
        
    def remove(self, target):
        if target and target.strip() in self.items:
            self.items.remove(target.strip())
            return True
        return False

try:
    line = input()
    if line.isdigit():
        n = int(line)
        items = [input() for _ in range(n)]
        target = input()
        
        inv = Inventory(items)
        if inv.is_valid and target.strip():
            if inv.remove(target):
                print("REMOVED")
            else:
                print("NOTFOUND")
        else:
            print("BAD")
    else:
        print("BAD")
except:
    print("BAD")