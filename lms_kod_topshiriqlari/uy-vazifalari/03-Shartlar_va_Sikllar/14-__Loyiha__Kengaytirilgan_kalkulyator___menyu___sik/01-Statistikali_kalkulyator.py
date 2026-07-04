amallar = 0
yigindi = 0

while True:
    k = int(input())
    if k == 0:
        break
        
    a = int(input())
    b = int(input())
    
    yaroqli = False
    natija = 0
    
    if k == 1:
        natija = a + b 
        yaroqli = True
    elif k == 2:
        natija = a - b 
        yaroqli = True
    elif k == 3:
        natija = a * b 
        yaroqli = True
    elif k == 4:
        if b != 0:
            natija = a // b 
            yaroqli = True
            
    if yaroqli:
        print(natija)
        amallar += 1
        yigindi += natija
        
print(f"Amallar: {amallar}")
print(f"Natijalar yig'indisi: {yigindi}")