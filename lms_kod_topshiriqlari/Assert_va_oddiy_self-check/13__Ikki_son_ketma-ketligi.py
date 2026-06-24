try:
    a = int(input())
    b = int(input())
    assert b > a
    print("OK")
except (AssertionError, ValueError):
    print("ERROR")