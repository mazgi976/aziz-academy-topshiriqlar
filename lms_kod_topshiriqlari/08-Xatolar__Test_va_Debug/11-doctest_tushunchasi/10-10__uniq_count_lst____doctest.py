import doctest

def uniq_count(lst):
    """
    >>> uniq_count([1, 1, 2])
    2
    >>> uniq_count([1, 2, 3])
    3
    >>> uniq_count([1, 1, 1])
    1
    """
    return len(set(lst))

if __name__ == "__main__":
    doctest.testmod()
    
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
        
    print(uniq_count(numbers))