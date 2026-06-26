import json

data = json.loads(input().strip())
print(data['app']['port'])