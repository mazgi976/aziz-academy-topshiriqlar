first = input()
last = input()

def make_full_name(first, last):
    return f"{first} {last}"

res1 = make_full_name(first, last)
res2 = make_full_name(last=last, first=first)

print(res1)
print(res2)