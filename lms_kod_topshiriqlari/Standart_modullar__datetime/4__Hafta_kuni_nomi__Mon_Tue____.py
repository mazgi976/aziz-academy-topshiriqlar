from datetime import date

s = input().strip()
d = date.fromisoformat(s)

names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(names[d.weekday()])