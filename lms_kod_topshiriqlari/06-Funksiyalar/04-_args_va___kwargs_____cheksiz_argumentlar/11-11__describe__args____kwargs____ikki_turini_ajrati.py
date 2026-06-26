def describe(*args, **kwargs):
    return {
            'args_count': len(args),
        'args_sum': sum(args),
        'kwargs_count': len(kwargs),
        'kwargs_sum': sum(kwargs.values())
    }
    
args_list = [int(x) for x in input().split()]

n = int(input())
kwargs_dict = {}
for _ in range(n):
    key, value = input().split()
    kwargs_dict[key] = int(value)
    
result = describe(*args_list, **kwargs_dict)
print(result)