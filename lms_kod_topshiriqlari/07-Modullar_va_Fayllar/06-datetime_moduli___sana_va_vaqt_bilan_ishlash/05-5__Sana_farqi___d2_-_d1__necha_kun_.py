from datetime import date

d1 = date.fromisoformat(input().strip())
d2 = date.fromisoformat(input().strip())

farq = (d2 - d1).days
print(farq)