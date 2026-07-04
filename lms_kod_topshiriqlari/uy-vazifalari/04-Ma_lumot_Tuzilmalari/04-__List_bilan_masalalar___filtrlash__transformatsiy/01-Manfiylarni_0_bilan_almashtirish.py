nums = list(map(int, input().split()))

for x in nums:
    if x < 0:
        print(0, end=" ")
    else:
        print(x, end=" ")