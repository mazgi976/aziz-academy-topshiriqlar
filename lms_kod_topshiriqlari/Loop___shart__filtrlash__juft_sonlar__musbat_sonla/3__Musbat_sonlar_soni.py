n = int(input())
sonlar = map(int, input().split())

print(len([x for x in sonlar if x > 0]))