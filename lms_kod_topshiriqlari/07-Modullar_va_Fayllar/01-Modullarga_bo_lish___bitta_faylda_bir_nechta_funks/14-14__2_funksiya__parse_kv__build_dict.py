def parse_kv(line):
    key, value = line.split('=')
    return key, int(value)

def build_dict(pairs):
    d = {}
    for key, value in pairs:
        d[key] = value
    return d

n = int(input())
pairs = []
for _ in range(n):
    line = input()
    pairs.append(parse_kv(line))
    
res_dict = build_dict(pairs)
print(res_dict)