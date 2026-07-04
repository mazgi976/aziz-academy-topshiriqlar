nums = input().split()

yigindi = 0

for i in range(len(nums)):
    if i % 2 == 0:
        yigindi += int(nums[i])
        
print(yigindi)