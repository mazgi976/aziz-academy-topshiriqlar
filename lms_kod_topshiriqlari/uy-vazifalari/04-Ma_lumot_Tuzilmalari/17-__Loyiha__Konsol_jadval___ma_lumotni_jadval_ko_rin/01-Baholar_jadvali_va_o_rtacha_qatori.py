N = int(input())
talabalar = []
yigindi = 0

for _ in range(N):
    ism, baho = input().split()
    baho = int(baho)
    talabalar.append({"name": ism, "score": baho})
    yigindi += baho
    
w = len("O'rtacha")
for talaba in talabalar:
    if len(talaba["name"]) > w:
        w = len(talaba["name"])
        
for talaba in talabalar:
    print(talaba["name"].ljust(w) + str(talaba["score"]).rjust(5))
    
ortacha = yigindi // N
print("O'rtacha".ljust(w) + str(ortacha).rjust(5))