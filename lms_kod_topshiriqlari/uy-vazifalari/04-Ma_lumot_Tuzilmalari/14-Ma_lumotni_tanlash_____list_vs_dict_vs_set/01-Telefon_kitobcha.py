n = int(input())

kitob = {}

for _ in range(n):
    ism, raqam = input().split()
    kitob[ism] = raqam
    
q = int(input())

for _ in range(q):
    ism = input()
    if ism in kitob:
        print(kitob[ism])
    else:
        print("topilmadi")