def avg(a, b=0, c=0):
    return (a + b + c)

nums = [int(n) for n in input().split()]
n_count = len(nums)

if n_count == 1:
    result = avg(nums[0]) / 1
elif n_count == 2:
    result = avg(nums[0], nums[1]) / 2
else:
    result = avg(nums[0], nums[1], nums[2]) / 3
    
print(f"{result:.2f}")