n = int(input())
i = 0

while i < n:
    i += 1
    if i % 2 == 0 and i % 3 == 0:
        continue
    print(i)