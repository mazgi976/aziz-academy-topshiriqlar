n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
    
idx = int(input())

try:
    element = lst[idx]
except IndexError:
    print('OUT')
else:
    print('OK')