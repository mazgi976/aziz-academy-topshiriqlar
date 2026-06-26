n = int(input())

for _ in range(n):
    ism, ball = input().split()
    if int(ball) > 60:
        print(f"{ism} {ball}")