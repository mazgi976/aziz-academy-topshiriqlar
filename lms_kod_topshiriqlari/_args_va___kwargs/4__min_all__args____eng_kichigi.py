def min_all(*args):
    return min(args)

nums = [int(x) for x in input().split()]
print(min_all(*nums))