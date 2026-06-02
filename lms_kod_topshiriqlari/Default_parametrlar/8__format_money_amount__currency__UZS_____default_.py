def format_money(amount, currency='UZS'):
    return f"{amount} {currency}"

tokens = input().split()

if len(tokens) == 1:
    print(format_money(int(tokens[0])))
else:
    print(format_money(int(tokens[0]), tokens[1]))