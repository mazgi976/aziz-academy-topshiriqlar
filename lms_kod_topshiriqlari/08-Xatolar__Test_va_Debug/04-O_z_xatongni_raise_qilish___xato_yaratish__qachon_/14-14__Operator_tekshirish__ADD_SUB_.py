try:
    op = input()
    if op not in ["ADD", "SUB"]:
        raise ValueError
    print("OK")
except ValueError:
    print("OPERR")