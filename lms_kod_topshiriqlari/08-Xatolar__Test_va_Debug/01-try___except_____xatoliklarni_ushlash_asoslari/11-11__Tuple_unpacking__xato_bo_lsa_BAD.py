try:
    a, b = input().split()
    print(f"{a}|{b}")
except ValueError:
    print('BAD')