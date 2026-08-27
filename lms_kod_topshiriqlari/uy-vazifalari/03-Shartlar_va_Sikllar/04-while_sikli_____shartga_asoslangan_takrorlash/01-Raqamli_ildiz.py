n = int(input())

while n >= 10:
    s = 0 
    temp = n 
    while temp > 0:
        s += temp % 10 
        temp //= 10 
    n = s 
    
print(n)