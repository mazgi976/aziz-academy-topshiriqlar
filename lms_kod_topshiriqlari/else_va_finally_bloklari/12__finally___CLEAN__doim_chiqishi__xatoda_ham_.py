mode = input()
out = ''

try:
    if mode == '1':
        out = 'OK'
    elif mode == '0':
        1 / 0 
except ZeroDivisionError:
    out = 'ERR'
finally:
    out = out + ' CLEAN'
            
print(out)