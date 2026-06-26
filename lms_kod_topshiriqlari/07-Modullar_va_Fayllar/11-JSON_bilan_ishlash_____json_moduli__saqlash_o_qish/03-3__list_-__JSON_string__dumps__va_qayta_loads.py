import json

n = int(input().strip())
my_list = []

for _ in range(n):
    my_list.append(int(input().strip()))
    
json_string = json.dumps(my_list)
reconstructed_list = json.loads(json_string)

print(sum(reconstructed_list))