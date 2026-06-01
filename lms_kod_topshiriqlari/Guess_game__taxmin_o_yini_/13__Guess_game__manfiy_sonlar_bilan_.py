secret = -4
while True:
    guess = int(input())
    if guess < secret:
        print("Low")
    elif guess > secret:
        print("High")
    else:
        print("Correct")
        break