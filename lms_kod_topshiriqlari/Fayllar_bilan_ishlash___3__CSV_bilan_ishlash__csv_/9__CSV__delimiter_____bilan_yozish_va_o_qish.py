n = int(input())
max_score = -1

for _ in range(n):
    ism, ball = input().split()
    ball = int(ball)
    if ball > max_score:
        max_score = ball
        
print(max_score)