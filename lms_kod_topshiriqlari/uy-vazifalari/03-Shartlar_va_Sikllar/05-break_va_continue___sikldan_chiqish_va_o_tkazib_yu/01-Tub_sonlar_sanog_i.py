tub_sonlar_soni = 0

while True:
    n = int(input())
    
    if n == 0:
        break
        
    if n < 2:
        continue
        
    tub = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            tub = False
            break
        i += 1
        
    if tub:
        tub_sonlar_soni += 1
        
print(tub_sonlar_soni)