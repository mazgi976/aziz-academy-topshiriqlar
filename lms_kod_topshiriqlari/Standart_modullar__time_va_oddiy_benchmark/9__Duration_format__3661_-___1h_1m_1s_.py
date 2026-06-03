s = int(input())

hh = s // 3600
mm = (s % 3600) // 60
ss = s % 60

print(f"{hh}h {mm}m {ss}s")