A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))

only_A = A - (B | C)
only_B = B - (A | C)
only_C = C - (A | B)

result = only_A | only_B | only_C 

if result:
    print(*sorted(result))
else:
    print("BO'SH")