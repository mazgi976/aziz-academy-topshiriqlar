from datetime import date

s = input().strip()
d = date.fromisoformat(s)

print(d.year)
print(d.month)
print(d.day)