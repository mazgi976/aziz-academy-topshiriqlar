from datetime import date

s = input().strip()
d = date.fromisoformat(s)

print(d.weekday())