nums = [int(c) for c in input().split()]
fahrenheit = [c * 9 // 5 + 32 for c in nums]
print(fahrenheit)