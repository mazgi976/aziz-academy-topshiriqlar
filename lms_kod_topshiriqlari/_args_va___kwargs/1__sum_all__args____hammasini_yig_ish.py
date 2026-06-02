def sum_all(*args):
    return sum(args)

nums = [int(x) for x in input().split()]
result = sum_all(*nums)
print(result)