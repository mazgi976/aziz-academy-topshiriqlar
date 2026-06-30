class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        if isinstance(amount, int) and amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

try:
    balance_input = input()
    amount_input = input()
    
    if balance_input.lstrip('-').isdigit() and amount_input.lstrip('-').isdigit():
        balance = int(balance_input)
        amount = int(amount_input)
        
        if balance >= 0:
            bank = Bank(balance)
            if bank.withdraw(amount):
                print(f"BAL={bank.balance}")
            else:
                print("BAD")
        else:
            print("BAD")
    else:
         print("BAD")
except:
    print("BAD")