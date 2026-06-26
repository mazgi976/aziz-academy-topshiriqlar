def inc(x, step=1):
    return x + step

nums = [int(n) for n in input().split()]

if len(nums) == 1:
    print(inc(nums[0]))
else:
    print(inc(nums[0], nums[1]))