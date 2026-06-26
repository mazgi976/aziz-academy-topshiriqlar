try:
    n = int(input())
    d = {}
    for _ in range(n):
        key, value = input().split()
        d[key] = value
        
    query_key = input()
    
    if query_key not in d:
        raise KeyError
    print("FOUND")
except KeyError:
    print("NOKEY")