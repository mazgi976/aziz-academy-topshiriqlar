n = int(input())
nums = [str(i) for i in range (1, n + 1) if i % 3 == 0]
if nums:
    print(*nums)
else:
    print("BO'SH")