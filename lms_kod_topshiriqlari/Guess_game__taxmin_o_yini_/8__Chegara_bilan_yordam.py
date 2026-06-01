s = 15
while True:
    g = int(input())
    if g == s:
        print("Correct")
        break
    if abs(s - g) > 5:
        print("Far")
    else:
        print("Close")