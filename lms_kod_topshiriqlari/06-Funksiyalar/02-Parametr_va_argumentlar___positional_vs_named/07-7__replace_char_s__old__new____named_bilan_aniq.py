s = input()
old = input()
new = input()

def replace_char(s, old, new):
    return s.replace(old, new)

res1 = replace_char(s, old, new)
res2 = replace_char(new=new, s=s, old=old)

print(res1)
print(res2)