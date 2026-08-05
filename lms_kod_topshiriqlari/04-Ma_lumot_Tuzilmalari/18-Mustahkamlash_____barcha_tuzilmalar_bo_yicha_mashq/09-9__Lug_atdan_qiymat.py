n = int(input())
d = {}
for _ in range(n):
    line = input().split()
    d[line[0]] = line[1]
    
target = input()
print(d[target])