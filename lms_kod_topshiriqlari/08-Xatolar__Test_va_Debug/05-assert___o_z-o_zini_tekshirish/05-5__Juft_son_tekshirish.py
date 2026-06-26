try:
    n = int(input())
    assert n % 2 == 0
    print("EVEN")
except (AssertionError, ValueError):
    print("ODD")