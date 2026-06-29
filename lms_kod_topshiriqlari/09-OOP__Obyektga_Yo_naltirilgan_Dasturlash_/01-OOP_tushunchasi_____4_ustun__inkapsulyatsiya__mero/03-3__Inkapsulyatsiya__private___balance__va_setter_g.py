try:
    balance = int(input())
    op = input().strip()
    amount = int(input())
    
    if balance < 0 or amount <= 0:
        print("BAD")
    else:
        if op == "DEPOSIT":
            print(f"BALANCE={balance + amount}")
        elif op == "WITHDRAW":
            if amount <= balance:
                print(f"BALANCE={balance - amount}")
            else:
                print("BAD")
        else:
            print("BAD")
except ValueError:
   print("BAD")