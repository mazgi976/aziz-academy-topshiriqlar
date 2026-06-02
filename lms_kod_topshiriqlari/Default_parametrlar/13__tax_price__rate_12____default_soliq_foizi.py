def tax(price, rate=12):
    return price * (1 + rate / 100)

nums = [int(n) for n in input().split()]

if len(nums) == 1:
    result = tax(nums[0])
else:
    result = tax(nums[0], nums[1])
    
print(f"{result:.2f}")