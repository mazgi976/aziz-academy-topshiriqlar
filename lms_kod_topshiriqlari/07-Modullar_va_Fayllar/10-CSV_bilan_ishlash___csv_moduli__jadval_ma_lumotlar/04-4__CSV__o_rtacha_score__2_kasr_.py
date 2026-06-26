n = int(input())
yigindi = 0

for _ in range(n):
    ism, ball = input().split()
    yigindi += int(ball)
    
o_rtacha = yigindi / n 
print(f"{o_rtacha:.2f}")