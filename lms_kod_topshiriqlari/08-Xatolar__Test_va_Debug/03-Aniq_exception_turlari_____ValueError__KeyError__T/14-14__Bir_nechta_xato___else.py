try:
    a = int(input())
    b = int(input())
    result = a + b
except ValueError:
    print("BAD")
except TypeError:
    print("TYPE")
else:
    print("OK")