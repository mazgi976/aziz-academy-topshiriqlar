def apply_op(op, *args):
    if op == 'sum':
        return sum(args)
    elif op == 'prod':
        result = 1
        for num in args:
            result *= num
        return result
    
op = input()
nums = [int(x) for x in input().split()]

print(apply_op(op, *nums))