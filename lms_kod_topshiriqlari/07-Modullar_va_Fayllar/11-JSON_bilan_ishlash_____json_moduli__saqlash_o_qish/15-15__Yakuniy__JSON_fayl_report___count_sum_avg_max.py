n = int(input())
scores = []

for _ in range(n):
    scores.append(int(input()))
    
count = len(scores)
total_sum = sum(scores)
avg = total_sum / count if count > 0 else 0
max_val = max(scores)

print(count)
print(total_sum)
print(f"{avg:.2f}")
print(max_val)