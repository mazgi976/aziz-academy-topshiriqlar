n = int(input())
yigindi = 0
maks_ball = -1

for _ in range(n):
    ism, ball = input().split()
    ball_int = int(ball)
    yigindi += ball_int
    if ball_int > maks_ball:
        maks_ball = ball_int
        
ortacha = yigindi / n
print(n)
print(yigindi)
print(f"{ortacha:.2f}")
print(maks_ball)