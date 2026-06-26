try:
    s = input()
    if not s.strip():
        raise ValueError
    print("OK")
except ValueError:
    print("EMPTY")