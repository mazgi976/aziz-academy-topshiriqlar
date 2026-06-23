import json

try:
    s = input()
    json.loads(s)
    print("OK")
except json.JSONDecodeError:
    print("INVALID")
except TypeError:
    print("TYPE")
except:
    print("TYPE")