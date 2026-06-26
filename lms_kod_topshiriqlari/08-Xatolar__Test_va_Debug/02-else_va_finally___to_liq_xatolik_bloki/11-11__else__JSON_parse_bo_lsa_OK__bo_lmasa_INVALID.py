import json

text = input()

try:
    json.loads(text)
except json.JSONDecodeError:
    print('INVALID')
else:
    print('OK')