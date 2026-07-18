nums = list(map(int, input().split()))
nums.sort()
n = len(nums)

ortacha = round(sum(nums) / n, 2)

if n % 2 != 0:
    mediana = nums[n // 2]
else:
    mediana = (nums[n // 2 - 1] + nums[n // 2]) // 2
    
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
    
max_count = max(counts.values())
modes = [key for key, val in counts.items() if val == max_count]
moda = min(modes)

print(f"O'rtacha: {ortacha}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")