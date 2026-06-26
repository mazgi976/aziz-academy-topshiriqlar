from datetime import date

s = input().strip()
d = date.fromisoformat(s)

if d.weekday() < 5:
    print("WORKDAY")
else:
    print("WEEKEND")