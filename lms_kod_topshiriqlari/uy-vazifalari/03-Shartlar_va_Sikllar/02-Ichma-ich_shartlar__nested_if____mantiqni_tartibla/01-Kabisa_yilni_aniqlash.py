year = int(input())

if year % 4 != 0:
    print("Kabisa emas")
else:
    if year % 100 != 0:
        print("Kabisa")
    else:
        if year % 400 == 0:
            print("Kabisa")
        else:
            print("Kabisa emas")