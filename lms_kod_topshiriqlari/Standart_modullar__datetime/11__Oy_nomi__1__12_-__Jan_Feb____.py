from datetime import date

s = input().strip()
d = date.fromisoformat(s)

names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print(names[d.month - 1])