def rename_keys(prefix='', **kwargs):
    return {prefix + k: v for k, v in kwargs.items()}

prefix = input()
n = int(input())
data = {}

for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
    
result = rename_keys(prefix=prefix, **data)
print(result)