set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))

umumiy = set1 & set2 & set3

print(*(sorted(list(umumiy))))