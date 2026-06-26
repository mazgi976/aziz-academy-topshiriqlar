import time

t = int(input())
tm = time.gmtime(t)

kunlar = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(kunlar[tm.tm_wday])