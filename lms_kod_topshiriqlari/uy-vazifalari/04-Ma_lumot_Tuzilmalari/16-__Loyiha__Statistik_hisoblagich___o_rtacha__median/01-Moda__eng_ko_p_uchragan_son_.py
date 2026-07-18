nums = list(map(int, input().split()))
counts = {}

for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
        
moda = max(counts, key=counts.get)
print(moda)