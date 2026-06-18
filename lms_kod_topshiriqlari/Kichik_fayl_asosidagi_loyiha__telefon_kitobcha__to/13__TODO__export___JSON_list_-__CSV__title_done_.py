n = int(input())
done_count = 0

for _ in range(n):
    line = input().split()
    if line[-1] == '1':
        done_count += 1
        
print(done_count)