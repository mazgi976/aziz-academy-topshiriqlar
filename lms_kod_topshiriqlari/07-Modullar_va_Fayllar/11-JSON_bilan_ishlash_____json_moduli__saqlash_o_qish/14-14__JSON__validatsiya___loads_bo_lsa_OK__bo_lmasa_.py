import json

try:
    json.loads(input())
    print("OK")
except:
    print("NO")