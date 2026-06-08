import json

n = int(input().strip())
my_list = []

for _ in range(n):
    line = input().split()
    my_list.append({"name": line[0], "score": int(line[1])})
    
json_text = json.dumps(my_list, ensure_ascii=False, sort_keys=True)
data = json.loads(json_text)

total_score = sum(item['score'] for item in data)
print(total_score)