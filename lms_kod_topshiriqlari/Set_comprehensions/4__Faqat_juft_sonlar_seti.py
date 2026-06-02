nums = list(map(int, input().split()))
even_set = sorted({x for x in nums if x % 2 == 0})

if even_set:
    print(*even_set)
else:
    print("BO'SH")