try:
    password = input()
    assert len(password) >= 6
    print("OK")
except AssertionError:
    print("WEAK")