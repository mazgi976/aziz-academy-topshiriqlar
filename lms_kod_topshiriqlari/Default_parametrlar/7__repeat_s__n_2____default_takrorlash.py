def repeat(s, n=2):
    return s * n

s = input()
second_line = input()

if second_line.strip() == "":
    print(repeat(s))
else:
    print(repeat(s, int(second_line)))