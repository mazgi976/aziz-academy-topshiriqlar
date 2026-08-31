yigindi = 0

while True:
    son = int(input())
    
    if son == 0 or son > 100:
        break
    elif son < 0:
        continue
        
    yigindi += son
    
print(yigindi)