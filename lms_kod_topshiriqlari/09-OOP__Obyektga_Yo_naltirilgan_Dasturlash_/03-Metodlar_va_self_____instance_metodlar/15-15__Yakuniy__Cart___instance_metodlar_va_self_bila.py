class Cart:
    def __init__(self):
        self.items = {}
        
    def add(self, name, price, qty):
        if not name or price < 0 or qty <= 0:
            return False
        
        if name in self.items:
            if self.items[name][0] != price:
                return False
            self.items[name][1] += qty
        else:
            self.items[name] = [price, qty]
        return True

    def total(self):
        return sum(item[0] * item[1] for item in self.items.values())
    
try:
    q_input = input()
    if not q_input.isdigit():
        print("BAD")
    else:
        q = int(q_input)
        cart = Cart()
        for _ in range(q):
            cmd_line = input().split()
            if not cmd_line:
                print("BAD")
                break
                
            if cmd_line[0] == "ADD":
                if len(cmd_line) != 4:
                    print("BAD")
                    break
                name, price, qty = cmd_line[1], int(cmd_line[2]), int(cmd_line[3])
                if not cart.add(name, price, qty):
                    print("BAD")
                    break
            elif cmd_line[0] == "TOTAL":
                print(cart.total())
            else:
                print("BAD")
                break
except:
    print("BAD")