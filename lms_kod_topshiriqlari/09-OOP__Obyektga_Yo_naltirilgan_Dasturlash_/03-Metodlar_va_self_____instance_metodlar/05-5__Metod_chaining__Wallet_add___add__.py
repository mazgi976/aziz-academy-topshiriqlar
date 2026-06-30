class Wallet:
    def __init__(self, balance):
        self.is_valid = isinstance(balance, int) and balance >= 0
        self.balance = balance if self.is_valid else 0
    def add(self, x):
        if self.is_valid and isinstance(x, int) and x >= 0:
            self.balance += x
        else:
            self.is_valid = False
        return self
    
try:
    balance_input = input()
    a_input = input()
    b_input = input()
    
    if balance_input.isdigit() and a_input.isdigit() and b_input.isdigit():
        w = Wallet(int(balance_input))
        w.add(int(a_input)).add(int(b_input))
        
        if w.is_valid:
            print(w.balance)
        else:
            print("BAD")
    else:
        print("BAD")
except:
    print("BAD")