kwh = int(input())

if kwh < 0:
    print("Notogri qiymat")
elif kwh <= 100:
    print(kwh * 450)
elif kwh <= 200:
    print(100 * 450 + (kwh - 100) * 600)
else:
    print(100 * 450 + 100 * 600 + (kwh - 200) * 900)