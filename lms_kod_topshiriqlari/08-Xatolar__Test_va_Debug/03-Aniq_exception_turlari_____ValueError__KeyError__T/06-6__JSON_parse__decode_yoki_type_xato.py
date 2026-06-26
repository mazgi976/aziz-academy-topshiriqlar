import json

try:
    s = input()
    
    if s == "":
        raise TypeError
        
    json.loads(s)
    print("OK")
    
except TypeError:
    print("TYPE")
except json.JSONDecodeError:
    print("INVALID")