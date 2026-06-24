try:
    age = int(input())
    if age < 18:
        raise ValueError
    print("ALLOWED")
except ValueError:
    print("DENIED")