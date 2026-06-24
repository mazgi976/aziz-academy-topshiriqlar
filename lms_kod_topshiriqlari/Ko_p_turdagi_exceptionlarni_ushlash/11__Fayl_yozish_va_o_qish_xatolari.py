try:
    mode = int(input())
    if mode == 1:
        print("ok")
    elif mode == 0:
        raise FileNotFoundError
except FileNotFoundError:
    print("NOFILE")
except PermissionError:
    print("NOPERM")
except ValueError:
    pass