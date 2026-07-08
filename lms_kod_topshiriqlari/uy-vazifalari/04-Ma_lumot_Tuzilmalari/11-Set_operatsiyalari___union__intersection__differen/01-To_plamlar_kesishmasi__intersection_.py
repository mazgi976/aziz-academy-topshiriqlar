qator1 = input().split()
qator2 = input().split()

set1 = set(map(int, qator1))
set2 = set(map(int, qator2))

natija = sorted(list(set1.intersection(set2)))

print(*natija)