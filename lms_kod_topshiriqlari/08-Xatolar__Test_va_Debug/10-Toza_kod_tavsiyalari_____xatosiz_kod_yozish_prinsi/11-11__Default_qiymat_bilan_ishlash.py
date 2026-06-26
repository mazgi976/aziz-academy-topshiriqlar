try:
    s = input()
except EOFError:
    print("N/A")
else:
    if s:
        print(s)
    else:
        print("N/A")