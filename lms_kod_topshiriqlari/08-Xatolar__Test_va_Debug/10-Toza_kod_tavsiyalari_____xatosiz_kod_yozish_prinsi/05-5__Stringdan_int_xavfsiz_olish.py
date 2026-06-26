s = input()

try:
    print(int(s) * 2)
except ValueError:
    print("BAD")