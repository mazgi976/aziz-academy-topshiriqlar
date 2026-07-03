yigindi = 0

while True:
    n = int(input())
    
    if n == 0 or n > 100:
        break
        
    if n < 0:
        continue
        
    yigindi += n
print(yigindi)