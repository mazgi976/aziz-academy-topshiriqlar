try:
    n = int(input())
    data = {}
    for _ in range(n):
        key, value = input().split()
        data[key] = value
        
    query = input()
    assert query in data
    print("FOUND")
except (AssertionError, ValueError, KeyError):
    print("NOKEY")