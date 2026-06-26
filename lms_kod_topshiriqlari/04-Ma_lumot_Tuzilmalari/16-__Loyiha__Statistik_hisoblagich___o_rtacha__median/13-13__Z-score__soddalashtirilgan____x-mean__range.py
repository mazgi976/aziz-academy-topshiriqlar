sonlar = [int(x) for x in input().split()]
mean = sum(sonlar) / len(sonlar)
diff = max(sonlar) - min(sonlar)

if diff == 0:
        z_scores = [f"{0.00:.2f}" for x in sonlar]
else:
    z_scores = [f"{(x - mean) / diff:.2f}" for x in sonlar]
            
print(*(z_scores))