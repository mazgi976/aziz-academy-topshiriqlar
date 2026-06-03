n = int(input())

max_num = int(input())
for _ in range(n - 1):
    num = int(input())
    if num > max_num:
        max_num = num
        
print(max_num)