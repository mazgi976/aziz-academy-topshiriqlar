class Account:
    def __init__(self, balance):
        if isinstance(balance, int) and balance >= 0:
            self._balance = balance
        else:
            self._balance = -1
            
    def get_balance(self):
        if self._balance != -1:
            return self._balance
        else:
            return "BAD"
        
try:
    balance_input = int(input())
    account = Account(balance_input)
    print(account.get_balance())
except ValueError:
    print("BAD")