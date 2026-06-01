total_sum = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num < 0:
        continue
    total_sum += num
    
print(total_sum)