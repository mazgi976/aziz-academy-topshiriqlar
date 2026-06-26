try:
    a = int(input())
    b = int(input())
    res = a // b
except ZeroDivisionError:
    print('DIV0')
else:
    print(res)