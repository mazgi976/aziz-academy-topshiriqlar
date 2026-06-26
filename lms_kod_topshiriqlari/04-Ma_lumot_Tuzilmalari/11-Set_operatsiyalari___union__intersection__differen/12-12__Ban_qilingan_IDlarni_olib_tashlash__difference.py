ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()  
result = ids - banned 

if result:
    print(*sorted(result))
else:
    print("BO'SH")