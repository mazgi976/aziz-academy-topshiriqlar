d = {}
for _ in range(3):
    n, p = input().split()
    d[n] = p

del_name = input()
if del_name in d:
    del d[del_name]
        
for n in sorted(d):
        print(n, d[n])