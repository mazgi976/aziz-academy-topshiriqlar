def scale_all(factor, *args):
    return [num * factor for num in args]

factor = int(input())
nums = [int(x) for x in input().split()]

result = scale_all(factor, *nums)
print(*result)