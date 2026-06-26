try:
    s = input().encode('cp1251')
    s.decode('utf-8')
    print("OK")
except UnicodeDecodeError:
    print("DECODE_ERROR")