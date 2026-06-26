try:
    s = input()
    assert 3 <= len(s) <= 10
    print("OK")
except AssertionError:
    print("ERROR")