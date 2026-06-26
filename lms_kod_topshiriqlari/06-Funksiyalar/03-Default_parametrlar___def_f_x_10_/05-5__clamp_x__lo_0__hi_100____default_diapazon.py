def clamp(x, lo=0, hi=100):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
    
nums = [int(n) for n in input().split()]

if len(nums) == 1:
    print(clamp(nums[0]))
elif len(nums) == 2:
    print(clamp(nums[0], nums[1]))
else:
    print(clamp(nums[0], nums[1], nums[2]))