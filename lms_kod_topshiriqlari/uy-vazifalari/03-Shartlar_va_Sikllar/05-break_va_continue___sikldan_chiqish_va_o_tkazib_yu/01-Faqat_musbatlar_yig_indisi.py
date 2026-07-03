n = int(input())
yigindi = 0
sanoq = 0

while sanoq < n:
    son = int(input())
    sanoq += 1
    
    if son <= 0:
        continue
        
    yigindi += son
    
print(yigindi)