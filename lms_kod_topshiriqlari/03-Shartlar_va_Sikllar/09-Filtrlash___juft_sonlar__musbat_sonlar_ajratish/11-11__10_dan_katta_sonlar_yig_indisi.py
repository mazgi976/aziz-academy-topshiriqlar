input()
sonlar = map(int, input().split())
print(sum(x for x in sonlar if x > 10))