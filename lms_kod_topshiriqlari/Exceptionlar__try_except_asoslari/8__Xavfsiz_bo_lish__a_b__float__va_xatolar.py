try:
    print("{:.2f}".format(float(input()) / float(input())))
except ValueError: print('BAD')
except ZeroDivisionError: print('DIV0')