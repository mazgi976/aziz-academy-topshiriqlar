try:
    n = int(input())
    d = {}
    for _ in range(n):
        key, value = input().split()
        d[key] = value
    query_key = input()
    print(int(d[query_key]))
except KeyError:
    print("NOKEY")
except ValueError:
    print("BADVAL")