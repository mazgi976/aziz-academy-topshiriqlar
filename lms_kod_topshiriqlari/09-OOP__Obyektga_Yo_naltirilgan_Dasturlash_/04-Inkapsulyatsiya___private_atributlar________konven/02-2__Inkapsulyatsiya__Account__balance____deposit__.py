class Account:
    def __init__(self, balance):
        if isinstance(balance, int) and balance >= 0:
            self._balance = balance
        else:
            self._balance = -1
            
    def deposit(self, amount):
        if self._balance != -1 and isinstance(amount, int) and amount > 0:
            self._balance += amount
            print(f"BAL={self._balance}")
        else:
            print("BAD")
            
balance_input = int(input())
amount_input = int(input())

account = Account(balance_input)
account.deposit(amount_input)