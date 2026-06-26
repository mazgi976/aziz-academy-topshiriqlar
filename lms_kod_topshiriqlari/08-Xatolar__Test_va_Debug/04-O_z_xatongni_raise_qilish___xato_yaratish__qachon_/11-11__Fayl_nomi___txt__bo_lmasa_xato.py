try:
    filename = input()
    if not filename.endswith('.txt'):
        raise ValueError
    print("OK")
except ValueError:
    print("BAD")