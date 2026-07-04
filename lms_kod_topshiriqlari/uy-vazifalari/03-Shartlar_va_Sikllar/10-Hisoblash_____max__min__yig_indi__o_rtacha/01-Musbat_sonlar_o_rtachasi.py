n = int(input())
yigindi = 0
soni = 0

for i in range(n):
    son = int(input())
    if son > 0:
        yigindi += son
        soni += 1
        
if soni == 0:
    print(0)
else:
    print(yigindi // soni)