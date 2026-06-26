try:
    n = int(input())
    if n % 2 != 0:
        raise ValueError
    print("EVEN")
except ValueError:
    print("ODD")