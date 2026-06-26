yigindi = 0
sanoq = 0

while True:
    son = int(input())
    if son == 0:
        break
    yigindi += son
    sanoq += 1
    
if sanoq == 0:
    print(0)
else:
    print(yigindi / sanoq)
        
    