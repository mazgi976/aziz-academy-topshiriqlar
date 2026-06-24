try:
    n = int(input())
    d = {}
    for _ in range(n):
        key, value = input().split()
        d[key] = int(value)
        
    a, b = input().split()
    print(d[a] // d[b])
except KeyError:
    print("NOKEY")
except ZeroDivisionError:
    print("DIV0")