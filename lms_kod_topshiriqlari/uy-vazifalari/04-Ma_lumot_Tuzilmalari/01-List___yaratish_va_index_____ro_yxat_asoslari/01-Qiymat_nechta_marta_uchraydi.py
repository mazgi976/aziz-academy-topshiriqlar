nums = input().split()
v = input()

count = 0
for x in nums:
    if x == v:
        count += 1
        
print(count)