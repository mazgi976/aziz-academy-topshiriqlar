class Account:
    def __init__(self, balance):
        if isinstance(balance, int) and balance >= 0:
            self._balance = balance
        else:
            self._balance = -1
            
    def set_balance(self, new_balance):
        if isinstance(new_balance, int) and new_balance >= 0:
            self._balance = new_balance
            print(f"BAL={self._balance}")
        else:
            print("BAD")
            
try:
    balance_input = int(input())
    new_balance_input = int(input())
    account = Account(balance_input)
    account.set_balance(new_balance_input)
except ValueError:
    print("BAD")