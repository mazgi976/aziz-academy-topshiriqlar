try:
    a = int(input())
    b = int(input())
    if b == 0:
        raise ZeroDivisionError
    print(a // b)
except ZeroDivisionError:
    print("DIV0")