n = int(input())
lst = list(map(int, input().split()))

start_index = (n + 1) // 2 
print(lst[start_index:])