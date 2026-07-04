n = int(input())
max_son = int(input())

for i in range(n - 1):
    joriy_son = int(input())
    if joriy_son > max_son:
        max_son = joriy_son
        
print(max_son)