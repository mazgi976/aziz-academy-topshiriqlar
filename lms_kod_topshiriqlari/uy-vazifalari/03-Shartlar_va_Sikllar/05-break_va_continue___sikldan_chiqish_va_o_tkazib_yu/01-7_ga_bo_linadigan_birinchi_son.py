N = int(input())
topildi = False

for _ in range(N):
    son = int(input())
    if son % 7 == 0:
        print(son)
        topildi = True
        break
        
if not topildi:
    print("yo'q")