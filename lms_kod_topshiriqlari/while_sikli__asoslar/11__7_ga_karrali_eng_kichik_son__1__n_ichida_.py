n = int(input())
son = 1
topildi = False

while son <= n:
    if son % 7 == 0:
        print(son)
        topildi = True
        break
    son += 1
if not topildi:
    print("No")
        