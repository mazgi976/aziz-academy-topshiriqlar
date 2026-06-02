def stats(nums):
    return {
            'count': len(nums),
        'sum': sum(nums),
        'min': min(nums),
        'max': max(nums)
    }
    
nums = list(map(int, input().split()))
print(stats(nums))