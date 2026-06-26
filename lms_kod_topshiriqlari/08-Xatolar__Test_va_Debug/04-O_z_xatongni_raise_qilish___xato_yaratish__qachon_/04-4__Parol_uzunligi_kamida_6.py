try:
    password = input()
    if len(password) < 6:
        raise ValueError
    print("OK")
except ValueError:
    print("WEAK")