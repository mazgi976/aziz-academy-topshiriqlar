try:
    print(int(input()) // int(input()))
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")