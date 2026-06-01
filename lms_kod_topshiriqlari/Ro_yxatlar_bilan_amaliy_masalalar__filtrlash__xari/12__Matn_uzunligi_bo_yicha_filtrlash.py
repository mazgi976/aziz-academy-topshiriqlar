n = int(input())
lst = input().split()

res = [x for x in lst if len(x) >= n]
print(res)