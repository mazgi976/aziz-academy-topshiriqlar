import json

json_string = input().strip()
my_dict = json.loads(json_string)

values = [str(my_dict[key]) for key in sorted(my_dict.keys())]

print(" ".join(values))