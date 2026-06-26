import json

data = json.loads(input().strip())
new_key = input().strip()
new_value = input().strip()

data[new_key] = new_value

print(json.dumps(data, ensure_ascii=False, sort_keys=True))