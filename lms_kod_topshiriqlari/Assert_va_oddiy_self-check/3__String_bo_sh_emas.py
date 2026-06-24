try:
    s = input()
    assert len(s.strip()) > 0
    print("OK")
except AssertionError:
    print("EMPTY")