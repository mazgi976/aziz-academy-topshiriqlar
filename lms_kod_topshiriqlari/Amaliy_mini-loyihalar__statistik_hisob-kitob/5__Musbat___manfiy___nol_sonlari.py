sonlar = [int(x) for x in input().split()]
positives = [x for x in sonlar if x > 0]
negatives = [x for x in sonlar if x < 0]
zeros = [x for x in sonlar if x == 0]

print(len(positives))
print(len(negatives))
print(len(zeros))