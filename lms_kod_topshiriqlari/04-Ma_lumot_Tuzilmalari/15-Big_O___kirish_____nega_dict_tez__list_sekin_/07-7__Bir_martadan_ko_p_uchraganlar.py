from collections import Counter

nums = input().split()
counts = Counter(nums)
print(sum(1 for count in counts.values() if count > 1))