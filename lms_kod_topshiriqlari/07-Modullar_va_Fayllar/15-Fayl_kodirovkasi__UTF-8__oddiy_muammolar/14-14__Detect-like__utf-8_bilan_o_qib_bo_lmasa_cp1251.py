mode, text = input(), input()
print(text.encode(mode.replace('utf8', 'utf-8')).decode(mode.replace('utf8', 'utf-8')))