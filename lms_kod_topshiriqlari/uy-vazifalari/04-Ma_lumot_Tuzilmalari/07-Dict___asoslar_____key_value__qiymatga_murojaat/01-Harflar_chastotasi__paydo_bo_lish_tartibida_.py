s = input()
hisob = {}

for harf in s:
    if harf in hisob:
        hisob[harf] += 1
    else:
        hisob[harf] = 1
        
for harf, son in hisob.items():
    print(f"{harf} {son}")