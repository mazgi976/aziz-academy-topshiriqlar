try:
    age = int(input())
    password = input()
    assert age >= 18
    assert len(password) >= 6
    print("ACCEPT")
except (AssertionError, ValueError):
    print("REJECT")