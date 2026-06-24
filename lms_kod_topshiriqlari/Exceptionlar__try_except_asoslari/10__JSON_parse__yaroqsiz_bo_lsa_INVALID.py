import json
try:
    json.loads(input())
    print('OK')
except json.JSONDecodeError:
    print('INVALID')