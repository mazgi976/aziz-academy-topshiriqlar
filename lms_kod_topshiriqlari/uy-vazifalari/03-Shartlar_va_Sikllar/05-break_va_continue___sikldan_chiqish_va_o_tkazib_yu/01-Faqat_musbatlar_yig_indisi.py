N = int(input())
yigindi = 0
sanoq = 0

while sanoq < N:
    n = int(input())
    sanoq += 1
    
    if n <= 0:
        continue
        
    yigindi += n
print(yigindi)