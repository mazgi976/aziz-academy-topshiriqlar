import json

n = int(input())
result = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    result[name] = result.get(name, 0) + score
    
print(json.dumps(result, sort_keys=True, ensure_ascii=False))