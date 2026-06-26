try:
    n = int(input())
    if n <= 0:
        raise ValueError
    print("OK")
except ValueError:
    print("ERROR")