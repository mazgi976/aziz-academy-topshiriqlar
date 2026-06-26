def prod_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

nums = [int(x) for x in input().split()]
print(prod_all(*nums))