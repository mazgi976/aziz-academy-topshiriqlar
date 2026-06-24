try:
    age = int(input())
    assert age >= 18
    print("ALLOWED")
except (AssertionError, ValueError):
    print("DENIED")