k = int(input())
config = {}

for _ in range(k):
    data = input().split()
    key = data[0]
    value = int(data[1])
    config[key] = value
    
q = int(input())

for _ in range(q):
    query_key = input()
    print(config.get(query_key, 0))