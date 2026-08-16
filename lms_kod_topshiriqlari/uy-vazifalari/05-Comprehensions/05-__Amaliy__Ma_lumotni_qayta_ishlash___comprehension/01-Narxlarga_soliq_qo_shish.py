prices = [int(p) for p in input().split()]
result = [p + p * 12 // 100 for p in prices]
print(result)