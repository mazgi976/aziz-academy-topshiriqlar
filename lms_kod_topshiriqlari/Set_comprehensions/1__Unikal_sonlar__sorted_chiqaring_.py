nums = list(map(int, input().split()))
unique_name = sorted({x for x in nums})
print(*unique_name)