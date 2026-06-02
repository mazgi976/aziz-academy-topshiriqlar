sonlar = [int(x) for x in input().split()]
counts = {}

for x in sonlar:
    counts[x] = counts.get(x, 0) + 1
        
max_count = max(counts.values())
modes = [x for x, count in counts.items() if count == max_count]
        
print(min(modes))