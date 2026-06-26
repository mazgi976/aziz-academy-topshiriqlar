try:
    score = int(input())
    if score < 0 or score > 100:
        raise ValueError
    print("OK")
except ValueError:
    print("OUT")