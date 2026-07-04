n = int(input())
min_son = int(input())

for i in range(n - 1):
    joriy_son = int(input())
    if joriy_son < min_son:
        min_son = joriy_son
        
print(min_son)