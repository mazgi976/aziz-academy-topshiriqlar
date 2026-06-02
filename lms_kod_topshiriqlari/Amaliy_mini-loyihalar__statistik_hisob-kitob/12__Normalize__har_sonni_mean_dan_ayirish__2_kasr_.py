sonlar = [int(x) for x in input().split()]
mean = sum(sonlar) / len(sonlar)
diffs = [f"{(x - mean):.2f}" for x in sonlar]
print(*(diffs))