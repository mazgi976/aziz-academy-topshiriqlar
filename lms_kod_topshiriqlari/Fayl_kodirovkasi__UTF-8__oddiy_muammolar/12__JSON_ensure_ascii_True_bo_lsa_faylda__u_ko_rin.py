import json
print('YES' if '\\u' in json.dumps({"word": input()}, ensure_ascii=True) else 'NO')