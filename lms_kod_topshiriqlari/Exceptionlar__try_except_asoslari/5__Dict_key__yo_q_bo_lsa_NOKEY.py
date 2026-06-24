try:
    n = int(input())
    d = {}
    for _ in range(n):
        k, v = input().split()
        d[k] = int(v)
    print(d[input()])
except KeyError:
    print('NOKEY')