nums = list(map(int, input().split()))

copy_nums = nums.copy()
copy_nums.sort()

print(*nums)
print(*copy_nums)