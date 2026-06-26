try:
    n = int(input())
    if n == 0:
        raise ValueError
    for _ in range(n):
        input()
    print("OK")
except ValueError:
    print("EMPTY")