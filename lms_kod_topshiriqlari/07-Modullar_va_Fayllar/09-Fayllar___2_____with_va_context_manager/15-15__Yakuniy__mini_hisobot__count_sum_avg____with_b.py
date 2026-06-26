n = int(input())

count = 0
jami = 0

for _ in range(n):
    score = int(input())
    count += 1
    jami += score
    
avg = jami / count if count > 0 else 0.0
print(count)
print(jami)
print(f"{avg:.2f}")