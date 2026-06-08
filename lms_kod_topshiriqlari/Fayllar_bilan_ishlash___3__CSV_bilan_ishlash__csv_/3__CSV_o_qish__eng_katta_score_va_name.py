n = int(input())

max_ism = ""
max_ball = -1

for _ in range(n):
    ism, ball = input().split()
    ball = int(ball)
    
    if ball > max_ball:
        max_ball = ball
        max_ism = ism
        
print(f"{max_ism} {max_ball}")