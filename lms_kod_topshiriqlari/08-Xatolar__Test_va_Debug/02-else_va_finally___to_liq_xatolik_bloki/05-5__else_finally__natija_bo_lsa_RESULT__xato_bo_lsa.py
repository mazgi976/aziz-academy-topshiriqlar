a = input()
b = input()

try:
    res = int(a) + int(b)
except ValueError:
    out = 'ERROR'
else:
    out = 'RESULT'
finally:
    out = out + '!'
    
print(out)