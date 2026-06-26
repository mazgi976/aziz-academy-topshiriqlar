a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a ^ b 

if result:
    print(*sorted(result))
else:
    print("BO'SH")