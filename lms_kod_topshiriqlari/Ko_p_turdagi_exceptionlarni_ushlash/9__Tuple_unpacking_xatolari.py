try:
    s = input()
    if not s.strip():
        print("TYPE")
    else:
        a, b = s.split()
        print(f"{a}|{b}")
except ValueError:
    print("BAD")
except Exception:
    print("TYPE")