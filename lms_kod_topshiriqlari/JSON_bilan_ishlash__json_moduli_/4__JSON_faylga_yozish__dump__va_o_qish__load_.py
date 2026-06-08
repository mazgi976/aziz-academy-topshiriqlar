import json

name = input().strip()
score = int(input().strip())

obj = {"name": name, "score": score}

json_string = json.dumps(obj, ensure_ascii=False, sort_keys=True)
data = json.loads(json_string)

print(data["name"], data["score"])