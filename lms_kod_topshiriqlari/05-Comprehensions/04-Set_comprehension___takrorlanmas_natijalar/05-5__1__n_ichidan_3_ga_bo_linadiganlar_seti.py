n = int(input())
multiples_of_three = sorted({x for x in range(1, n + 1) if x % 3 == 0})

if multiples_of_three:
    print(*multiples_of_three)
else:
    print("BO'SH")