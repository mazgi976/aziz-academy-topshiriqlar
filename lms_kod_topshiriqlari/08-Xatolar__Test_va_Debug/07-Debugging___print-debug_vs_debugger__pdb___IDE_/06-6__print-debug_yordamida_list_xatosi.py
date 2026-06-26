n = int(input())
yigindi = 0

for _ in range(n):
    try:
        son = int(input())
        yigindi += son
    except ValueError:
        continue
        
print(yigindi)