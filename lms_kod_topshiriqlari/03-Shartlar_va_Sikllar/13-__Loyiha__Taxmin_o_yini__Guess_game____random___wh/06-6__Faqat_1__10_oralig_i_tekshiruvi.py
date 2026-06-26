s = 6 
while True:
    g = int(input())
    if not (1 <= g <= 10):
        print("Invalid")
    elif g == s:
        print("Correct")
        break