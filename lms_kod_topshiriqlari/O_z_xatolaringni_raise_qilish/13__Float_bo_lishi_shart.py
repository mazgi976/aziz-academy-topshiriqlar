try:
    s = input()
    try:
        float(s)
    except ValueError:
        raise ValueError
    print("OK")
except ValueError:
    print("BAD")