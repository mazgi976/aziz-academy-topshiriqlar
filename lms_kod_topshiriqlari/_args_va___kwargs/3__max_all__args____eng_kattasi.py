def max_all(*args):
    return max(args)

nums = [int(x) for x in input().split()]
print(max_all(*nums))