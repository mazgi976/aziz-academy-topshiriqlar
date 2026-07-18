nums = list(map(int, input().split()))
nums.sort()
median = nums[len(nums) // 2]
print(median)