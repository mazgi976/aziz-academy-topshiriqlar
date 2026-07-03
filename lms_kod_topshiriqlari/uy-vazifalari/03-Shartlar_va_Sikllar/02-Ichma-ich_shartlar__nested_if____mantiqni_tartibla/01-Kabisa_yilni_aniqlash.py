yil = int(input())

if yil % 4 != 0:
    print("Kabisa emas")
else:
    if yil % 100 != 0:
        print("Kabisa")
    else:
        if yil % 400 == 0:
            print("Kabisa")
        else:
            print("Kabisa emas")