try:
    s = input().strip()
    if not s:
        print("EMPTY")
    else:
        print(len(s))
except EOFError:
    print("EMPTY")