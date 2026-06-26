n = int(input())
count = 0
i = 1

while i <= n:
    if i % 2 == 0:
        count += 1
        if count == 3:
            print(i)
            break
    i += 1
    
if count < 3:
    print("No")
        