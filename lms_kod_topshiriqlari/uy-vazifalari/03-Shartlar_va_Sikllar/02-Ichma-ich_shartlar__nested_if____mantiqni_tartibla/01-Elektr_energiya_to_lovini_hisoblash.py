kwh = int(input())

if kwh < 0:
    print("Notogri qiymat")
else:
    if kwh <= 100:
        total = kwh * 450
    elif kwh <= 200:
        total = 100 * 450 + (kwh - 100) * 600
    else:
        total = 100 * 450 + 100 * 600 + (kwh - 200) * 900
    print(total)