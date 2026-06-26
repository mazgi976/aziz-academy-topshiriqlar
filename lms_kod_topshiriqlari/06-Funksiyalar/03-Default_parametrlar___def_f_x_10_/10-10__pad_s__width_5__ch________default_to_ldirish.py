def pad(s, width=5, ch='.'):
    if len(s) >= width:
        return s
    return s + ch * (width - len(s))

s = input()
line2 = input().split()

if len(line2) == 0:
    print(pad(s))
elif len(line2) == 1:
    print(pad(s, width=int(line2[0])))
else:
    print(pad(s, width=int(line2[0]), ch=line2[1]))