import math

def mean(nums):
    return sum(nums) / len(nums)

def variance(nums):
    m = mean(nums)
    return sum((x - m) ** 2 for x in nums) / len(nums)

def std(nums):
    return math.sqrt(variance(nums))

nums = list(map(int, input().split()))

print(f"{mean(nums):.2f}")
print(f"{variance(nums):.2f}")
print(f"{std(nums):.2f}")