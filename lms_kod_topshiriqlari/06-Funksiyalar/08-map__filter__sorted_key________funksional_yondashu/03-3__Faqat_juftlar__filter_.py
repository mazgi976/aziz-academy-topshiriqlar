nums = map(int, input().split())
print(*(x for x in nums if x % 2 == 0))