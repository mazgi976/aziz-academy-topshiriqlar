try:
    s = input()
    if '+' in s:
        a, b = s.split('+')
        print(int(a) + int(b))
    elif '-' in s:
        a, b = s.split('-')
        print(int(a) - int(b))
    elif '*' in s:
        a, b = s.split('*')
        print(int(a) * int(b))
    elif '/' in s:
        a, b = s.split('/')
        if int(b) == 0:
            print("DIV0")
        else:
            print(int(a) // int(b))
    else:
        print(int(s))
except ZeroDivisionError:
    print("DIV0")
except:
    print("ERR")