n = int(input())
total_sum = 0
i = 0

while i < n:
    i += 1
    if i % 9 == 0:
        continue
    total_sum += i
    
print(total_sum)
