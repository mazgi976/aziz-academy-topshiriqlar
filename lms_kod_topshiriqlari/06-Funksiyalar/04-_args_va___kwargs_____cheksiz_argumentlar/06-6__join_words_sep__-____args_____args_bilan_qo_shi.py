def join_words(*args, sep='-'):
    return sep.join(args)

separator = input()
words = input().split()
print(join_words(*words, sep=separator))