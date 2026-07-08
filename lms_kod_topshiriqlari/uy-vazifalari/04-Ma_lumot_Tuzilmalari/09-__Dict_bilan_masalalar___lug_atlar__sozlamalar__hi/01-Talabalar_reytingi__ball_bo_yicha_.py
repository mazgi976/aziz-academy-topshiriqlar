n = int(input())
d = {}
for _ in range(n):
    ism, ball = input().split()
    d[ism] = int(ball)
    
reyting = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for ism, ball in reyting:
    print(f"{ism} {ball}")