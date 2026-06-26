s = 9
while True:
    g = int(input())
    if g < s:
        print("Low")
    elif g > s:
        print("High")
    else:
        print("Correct")
        break