n = int(input())
max_son = -float('inf')
max_index = -1

for i in range(1, n + 1):
    son = int(input())
    if son > max_son:
        max_son = son
        max_index = i 
        
print(max_index)