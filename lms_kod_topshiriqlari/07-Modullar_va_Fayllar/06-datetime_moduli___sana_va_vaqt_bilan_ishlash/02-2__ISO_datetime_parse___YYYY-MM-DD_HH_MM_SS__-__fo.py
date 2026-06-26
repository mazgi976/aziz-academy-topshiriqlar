from datetime import datetime

s = input().strip()
dt = datetime.fromisoformat(s)

print(dt.strftime('%Y/%m/%d %H:%M'))