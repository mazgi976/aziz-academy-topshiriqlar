n = int(input())
yigindi = 0

for _ in range(n):
    key, value = input().split()
    yigindi += int(value)
    
print(yigindi)