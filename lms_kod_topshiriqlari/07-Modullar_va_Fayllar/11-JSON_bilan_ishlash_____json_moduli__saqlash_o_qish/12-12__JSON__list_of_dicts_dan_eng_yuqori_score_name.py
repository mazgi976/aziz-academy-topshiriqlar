import json

n = int(input())
data_list = []

for _ in range(n):
    line = input().split()
    data_list.append({"name": line[0], "score": int(line[1])})
    
json_str = json.dumps(data_list)
data = json.loads(json_str)

best_player = max(data, key=lambda x: x['score'])

print(best_player['name'])