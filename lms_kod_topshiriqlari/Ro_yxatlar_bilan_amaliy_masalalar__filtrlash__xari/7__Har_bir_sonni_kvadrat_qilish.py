n = int(input())
lst = (list(map(int, input().split())))

res = [x**2 for x in lst]
print(res)