n = int(input())

yigindi = 0
for _ in range(n):
    qator = input()
    kalit, qiymat = qator.split("=")
    yigindi += int(qiymat)
    
print(yigindi)