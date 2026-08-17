def yigindi(oxir, boshlanish=1):
    return sum(range(boshlanish, oxir + 1))


oxir = int(input().strip())
boshlanish = int(input().strip())

print(yigindi(oxir))
print(yigindi(oxir, boshlanish))