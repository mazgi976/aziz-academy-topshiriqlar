s = input()
x = input()
z = s + " " + x
if len(z) == 14:
    v = int(len(z)) + 1
else:
    v = int(len(z))
print(f"Full name: {z}\nLength: {v}")