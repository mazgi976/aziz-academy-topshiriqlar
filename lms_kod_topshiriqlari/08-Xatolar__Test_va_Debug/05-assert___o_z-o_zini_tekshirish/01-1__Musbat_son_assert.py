try:
    n = int(input())
    assert n > 0
    print("OK")
except (AssertionError, ValueError):
    print("ERROR")