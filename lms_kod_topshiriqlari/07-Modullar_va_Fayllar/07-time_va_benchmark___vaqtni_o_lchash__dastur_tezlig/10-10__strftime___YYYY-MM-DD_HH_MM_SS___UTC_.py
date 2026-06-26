import time

t = int(input())
natija = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t))

print(natija)