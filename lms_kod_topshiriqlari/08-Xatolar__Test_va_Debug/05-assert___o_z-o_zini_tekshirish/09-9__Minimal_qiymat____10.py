try:
    n = int(input())
    assert n >= 10
    print("OK")
except (AssertionError, ValueError):
    print("SMALL")