def min2(a, b):
    return a if a < b else b

def max2(a, b):
    return a if a > b else b

ops = {
        'min2': min2,
    'max2': max2
}

min_fn = ops['min2']
max_fn = ops['max2']

a, b = map(int, input().split())

print(min_fn(a, b))
print(max_fn(a, b))