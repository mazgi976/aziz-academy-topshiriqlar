sonlar = [int(x) for x in input().split()]
count = len(sonlar)
s_sum = sum(sonlar)
s_min = min(sonlar)
s_max = max(sonlar)
mean = s_sum / count
evens = len([x for x in sonlar if x % 2 == 0])
odds = count - evens

print(f"count: {count}")
print(f"sum: {s_sum}")
print(f"min: {s_min}")
print(f"max: {s_max}")
print(f"mean: {mean:.2f}")
print(f"evens: {evens}")
print(f"odds: {odds}")