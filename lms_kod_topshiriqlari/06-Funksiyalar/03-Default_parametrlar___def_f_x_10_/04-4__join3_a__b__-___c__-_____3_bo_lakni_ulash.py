def join3(a, b='-', c='-'):
    return f"{a} {b} {c}"

words = input().split()

if len(words) == 1:
    print(join3(words[0]))
elif len(words) == 2:
    print(join3(words[0], words[1]))
else:
    print(join3(words[0], words[1], words[2]))