import json

n = int(input().strip())
my_list = []

for _ in range(n):
    line = input().split()
    my_list.append({"name": line[0], "score": int(line[1])})
    
data = json.loads(json.dumps(my_list))

count = 0
for item in data:
    if item['score'] >= 60:
        count += 1
        
print(count)