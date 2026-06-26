try:
    score = int(input())
    assert 0 <= score <= 100
    print("OK")
except (AssertionError, ValueError):
    print("OUT")