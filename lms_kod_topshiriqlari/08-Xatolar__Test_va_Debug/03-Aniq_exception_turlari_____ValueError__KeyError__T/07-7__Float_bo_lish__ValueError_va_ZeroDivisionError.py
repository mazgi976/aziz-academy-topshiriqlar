try:
    a = float(input())
    b = float(input())
    print(f"{a/b:.2f}")
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")