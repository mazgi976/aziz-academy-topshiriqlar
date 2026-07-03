tub_sonlar_soni = 0

while True:
    n = int(input())
    
    if n == 0:
        break
        
    if n < 2:
        continue
        
    is_tub = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_tub = False
            break
        i += 1
        
    if is_tub:
        tub_sonlar_soni += 1
        
print(tub_sonlar_soni)