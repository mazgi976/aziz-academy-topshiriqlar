n = int(input())
yigindi = 0

for _ in range(n):
    ism, ball = input().split()
    try:
        yigindi += int(ball)
    except ValueError:
        continue
        
print(yigindi)