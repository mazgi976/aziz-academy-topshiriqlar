n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = value
    
query_key = input()

try:
    v = d[query_key]
except KeyError:
    print('NOKEY')
else:
    print('VALUE')