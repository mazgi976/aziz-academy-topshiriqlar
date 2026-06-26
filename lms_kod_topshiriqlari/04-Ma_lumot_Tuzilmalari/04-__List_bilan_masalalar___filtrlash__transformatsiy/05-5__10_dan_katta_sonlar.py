n = int(input())
lst = list(map(int, input().split()))

res = [x for x in lst if x > 10]
print(res)