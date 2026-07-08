set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

natija = set1.symmetric_difference(set2)

print(*(sorted(list(natija))))