import json

data = json.loads(input().strip())

max_val = max(data.values())
result = sorted([k for k, v in data.items() if v == max_val])[0]

print(result)