s = 20 
c = 0

while True:
    g = int(input())
    c += 1
    
    if 1 <= g <= 20:      
        if g < s:
            print("Low")
        elif g > s:
            print("High")
        else:
             print("Correct")
             print(c)
             break
    else:
        print("Invalid")