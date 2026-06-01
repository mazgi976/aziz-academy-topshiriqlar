a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = b - a 

if result:
    print(*sorted(result))
else:
    print("BO'SH")