n = int(input())
yigindi = 0

for _ in range(n):
    ism, ball = input().split()
    yigindi += int(ball)
    
print(yigindi)