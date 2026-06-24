try:
    s = input()
    float(s)
    print("OK")
except ValueError:
    print("ERROR")