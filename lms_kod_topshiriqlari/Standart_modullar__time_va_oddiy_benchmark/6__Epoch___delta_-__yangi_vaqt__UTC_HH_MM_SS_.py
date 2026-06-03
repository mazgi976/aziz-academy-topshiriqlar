import time

t = int(input())
delta = int(input())

new_t = t + delta
tm = time.gmtime(new_t)

print(f"{tm.tm_hour:02d}:{tm.tm_min:02d}:{tm.tm_sec:02d}")