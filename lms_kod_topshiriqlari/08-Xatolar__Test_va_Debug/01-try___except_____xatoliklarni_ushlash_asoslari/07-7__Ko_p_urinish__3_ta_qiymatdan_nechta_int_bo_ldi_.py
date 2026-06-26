count = 0
for _ in range(3):
    try:
        int(input())
        count += 1
    except ValueError:
        pass
print(count)