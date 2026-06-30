class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        if not isinstance(self.balance, int) or self.balance < 0:
            return "BAD"
        if isinstance(amount, int) and amount > 0:
            self.balance += amount
            return self.balance
        return "BAD"

try:
    balance = int(input())
    amount = int(input())
    bank = Bank(balance)
    print(bank.deposit(amount))
except ValueError:
    print("BAD")