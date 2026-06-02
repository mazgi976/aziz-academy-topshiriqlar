def min_max(nums):
    return min(nums), max(nums)

nums = list(map(int, input().split()))
minimum, maximum = min_max(nums)

print(minimum)
print(maximum)