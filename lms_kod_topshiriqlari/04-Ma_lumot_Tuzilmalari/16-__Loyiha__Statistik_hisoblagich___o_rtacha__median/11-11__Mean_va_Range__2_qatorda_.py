sonlar = [int(x) for x in input().split()]
mean = sum(sonlar) / len(sonlar)
diff = max(sonlar) - min(sonlar)

print(f"{mean:.2f}")
print(diff)
