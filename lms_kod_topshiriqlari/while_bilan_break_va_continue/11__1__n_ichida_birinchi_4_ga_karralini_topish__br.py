n = int(input())
found = False
i = 1

while i <= n:
    if i % 4 == 0:
        print(i)
        found = True
        break
    i += 1    
    
if not found:
        print("No")
