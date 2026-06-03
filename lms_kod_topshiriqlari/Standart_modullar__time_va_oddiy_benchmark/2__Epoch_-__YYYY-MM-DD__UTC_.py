import time

t = int(input())
natija = time.strftime('%Y-%m-%d', time.gmtime(t))

print(natija)