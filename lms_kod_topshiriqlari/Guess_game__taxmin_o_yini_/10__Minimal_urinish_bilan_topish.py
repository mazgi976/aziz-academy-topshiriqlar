s = 1
c = 0
while True:
    g = int(input())
    c += 1
    if g == s:
        print("Correct")
        print(c)
        break
    else:
        print("Try again")