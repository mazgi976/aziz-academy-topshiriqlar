price = int(input()) 

if price >= 100:
    if price >= 500:
        print(price * 0.8)
    else:
        print(price * 0.9)
else:
    print(float(price))


