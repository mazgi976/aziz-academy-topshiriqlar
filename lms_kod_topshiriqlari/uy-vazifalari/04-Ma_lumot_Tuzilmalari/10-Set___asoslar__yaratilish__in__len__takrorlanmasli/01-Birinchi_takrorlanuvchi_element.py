seen = set()

for son in input().split():
    if son in seen:
        print(son)
        break
    seen.add(son)
else:
    print("Yo'q")