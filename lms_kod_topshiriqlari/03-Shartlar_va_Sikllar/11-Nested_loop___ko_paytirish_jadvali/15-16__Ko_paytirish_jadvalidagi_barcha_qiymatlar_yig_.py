n = int(input())
yigindi = 0 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        yigindi += i * j 
print(yigindi)