mode = input()
text = input()

try:
    if mode == '1':
        pass
    else:
        1 / 0 
except ZeroDivisionError:
    pass
finally:
    print('DONE')