try:
    n = int(input())
    if n < 10:
        raise ValueError
    print("OK")
except ValueError:
    print("SMALL")