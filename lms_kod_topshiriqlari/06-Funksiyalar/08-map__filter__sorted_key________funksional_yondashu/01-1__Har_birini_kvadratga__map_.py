nums = map(int, input().split())
print(*(x ** 2 for x in nums))