n = int(input())
lst = list(map(int, input().split()))

res = [abs(x) for x in lst]
print(res)