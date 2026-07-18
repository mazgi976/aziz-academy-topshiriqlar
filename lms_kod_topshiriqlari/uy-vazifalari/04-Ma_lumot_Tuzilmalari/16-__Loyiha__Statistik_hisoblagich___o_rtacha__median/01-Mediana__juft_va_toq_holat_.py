nums = list(map(int, input().split()))
nums.sort()
n = len(nums)

if n % 2 != 0:
    print(nums[n // 2])
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) // 2
    print(median)