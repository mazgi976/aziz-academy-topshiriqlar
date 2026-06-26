try:
    n = int(input())
    assert n > 0
    for _ in range(n):
        input()
    print("OK")
except (AssertionError, ValueError):
    print("EMPTY")