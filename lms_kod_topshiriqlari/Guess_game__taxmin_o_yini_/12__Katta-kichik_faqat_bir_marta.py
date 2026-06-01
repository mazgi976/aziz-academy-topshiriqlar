s = 8
c = 0
while True:
    g = int(input())
    c += 1
    if g == s:
        print("Correct")
        break
    if c == 1:
        if g < s: print("Low")
        else: print("High")
    else:
        print("Wrong")
        