n = int(input())
lugat = {}

for _ in range(n):
    ism, ball = input().split()
    ball = int(ball)
    if ism in lugat:
        lugat[ism] += ball
    else:
        lugat[ism] = ball
        
for ism in sorted(lugat.keys()):
    print(f"{ism} {lugat[ism]}")