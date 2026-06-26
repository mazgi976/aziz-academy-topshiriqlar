try:
    input().encode('ascii')
    print("OK")
except UnicodeEncodeError:
    print("ENCODE_ERROR")