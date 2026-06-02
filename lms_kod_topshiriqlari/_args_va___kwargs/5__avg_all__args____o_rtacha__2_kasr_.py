def avg_all(*args):
    return sum(args) / len(args)

nums = [int(x) for x in input().split()]
result = avg_all(*nums)
print(f"{result:.2f}")