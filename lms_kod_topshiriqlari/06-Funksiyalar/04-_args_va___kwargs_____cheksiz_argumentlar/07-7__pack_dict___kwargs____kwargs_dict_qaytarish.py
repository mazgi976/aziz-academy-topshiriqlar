def pack_dict(**kwargs):
    return kwargs

n = int(input())
temp_dict = {}

for _ in range(n):
    key, value = input().split()
    temp_dict[key] = int(value)
    
result = pack_dict(**temp_dict)
print(result)