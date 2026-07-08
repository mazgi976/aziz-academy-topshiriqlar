n = int(input())

jami = 0

for _ in range(n):
    data = input().split()
    jami += len(data) - 1
    
print(jami)