n = int(input())
topildi = False

while n > 0:
    son = int(input())
    if son % 7 == 0:
        print(son)
        topildi = True
        break
    n -= 1
    
if not topildi:
    print("yo'q")