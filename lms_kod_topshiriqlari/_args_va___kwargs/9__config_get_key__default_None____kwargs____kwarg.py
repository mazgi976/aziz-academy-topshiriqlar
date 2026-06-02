def config_get(key, default=None, **kwargs):
    return kwargs.get(key, default)

search_key = input()
n = int(input())
config_data = {}

for _ in range(n):
    k, v = input().split()
    config_data[k] = int(v)
    
result = config_get(search_key, default=0, **config_data)
print(result)