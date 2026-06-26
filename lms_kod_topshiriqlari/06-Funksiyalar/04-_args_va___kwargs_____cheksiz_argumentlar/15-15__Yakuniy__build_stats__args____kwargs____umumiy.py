def build_stats(*args, **kwargs):
    return {
            'count': len(args),
        'min': min(args),
        'max': max(args),
        'sum': sum(args),
        'extra_keys': sorted(kwargs.keys()),
        'extra_sum': sum(kwargs.values())
    }
    
args_list = [int(x) for x in input().split()]

n = int(input())
kwargs_dict = {}
for _ in range(n):
    key, value = input().split()
    kwargs_dict[key] = int(value)
    
result = build_stats(*args_list, **kwargs_dict)
print(result)