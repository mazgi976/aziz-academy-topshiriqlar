s = 10

for _ in range(5):
    g = int(input())
    if g == s:      
        print("Correct")
        break
else:
    print("You lost")