try:
    email = input()
    assert "@" in email 
    print("OK")
except AssertionError:
    print("BAD")