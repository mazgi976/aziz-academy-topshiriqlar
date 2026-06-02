def line(char='-', n=10):
    return char * n

tokens = input().split()

if len(tokens) == 0:
    print(line())
elif len(tokens) == 1:
    token = tokens[0]
    if token.isdigit():
        print(line(n=int(token)))
    else:
        print(line(char=token))
else:
    print(line(char=tokens[0], n=int(tokens[1])))