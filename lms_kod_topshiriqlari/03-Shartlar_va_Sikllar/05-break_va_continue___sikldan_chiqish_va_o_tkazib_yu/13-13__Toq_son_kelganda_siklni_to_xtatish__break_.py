total_sum = 0

while True:
    n = int(input())
    if n % 2 != 0:
        break
    total_sum += n
    
print(total_sum)