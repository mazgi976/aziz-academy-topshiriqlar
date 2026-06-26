s = input()
closed = False

try:
    int(s)
except ValueError:
    pass
finally:
    closed = True
        
if closed:
    print('YES')
else:
    print('NO')