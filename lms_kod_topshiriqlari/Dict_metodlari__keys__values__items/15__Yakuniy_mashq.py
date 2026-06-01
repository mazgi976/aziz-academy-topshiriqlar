fanlar = {}

while True:
    try:
        fan, baho = input().split()
        fanlar[fan] = int(baho)
    except:
         break
            
fan = max(fanlar, key=fanlar.get)
print(fan, fanlar[fan])