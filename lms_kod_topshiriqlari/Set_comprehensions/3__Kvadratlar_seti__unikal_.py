nums = list(map(int, input().split()))
squared_set = sorted({x**2 for x in nums})
print(*squared_set)