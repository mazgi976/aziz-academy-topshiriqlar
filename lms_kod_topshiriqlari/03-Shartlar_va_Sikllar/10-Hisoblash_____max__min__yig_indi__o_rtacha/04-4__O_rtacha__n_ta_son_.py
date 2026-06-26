n = int(input())
sonlar = list(map(int, input().split()))

s = 0
for x in sonlar:
    s += x
    
print(float(s / n))