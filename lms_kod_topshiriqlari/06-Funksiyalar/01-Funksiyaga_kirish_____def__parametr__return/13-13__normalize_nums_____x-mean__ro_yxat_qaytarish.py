def normalize(nums):
    mean = sum(nums) / len(nums)
    return [x - mean for x in nums]

nums = list(map(int, input().split()))
result = normalize(nums)

print(*(f"{val:.2f}" for val in result))