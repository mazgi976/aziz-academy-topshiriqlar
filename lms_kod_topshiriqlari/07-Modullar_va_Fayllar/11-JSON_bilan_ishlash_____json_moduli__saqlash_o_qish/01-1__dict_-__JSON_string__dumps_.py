import json

key = input().strip()
value = input().strip()

my_dict = {key: value}

json_string = json.dumps(my_dict, ensure_ascii=False, sort_keys=True)

print(json_string)