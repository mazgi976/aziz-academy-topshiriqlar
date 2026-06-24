try:
    email = input()
    if '@' not in email:
        raise ValueError
    print("OK")
except ValueError:
    print("BAD")