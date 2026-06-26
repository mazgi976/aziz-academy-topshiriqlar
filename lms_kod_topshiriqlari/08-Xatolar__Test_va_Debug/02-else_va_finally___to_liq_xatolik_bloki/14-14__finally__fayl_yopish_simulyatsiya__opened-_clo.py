mode = input()

opened = True
closed = False

try:
    if mode == '0':
        1 / 0 
except ZeroDivisionError:
    pass
finally:
    opened = False
    closed = True
            
if opened == False and closed == True:
    print('YES')
else:
    print('NO')