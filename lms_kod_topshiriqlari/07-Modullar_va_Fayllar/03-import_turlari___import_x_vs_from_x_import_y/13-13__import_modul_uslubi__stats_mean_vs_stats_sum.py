def ssum(nums):
    return sum(nums)

def mean(nums):
    return sum(nums) / len(nums) if nums else 0

stats = {'sum': ssum, 'mean': mean}

def main():
    nums = list(map(int, input().split()))
    
    total = stats['sum'](nums)
    avg = stats['mean'](nums)
    
    print(total)
    print(f"{avg:.2f}")
    
if __name__ == '__main__':
    main()