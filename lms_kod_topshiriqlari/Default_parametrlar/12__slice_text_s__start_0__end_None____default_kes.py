def slice_text(s, start=0, end=None):
    return s[start:end]

s = input()
line2 = input().split()

if len(line2) == 0:
    print(slice_text(s))
elif len(line2) == 1:
    print(slice_text(s, start=int(line2[0])))
else:
    print(slice_text(s, start=int(line2[0]), end=int(line2[1])))