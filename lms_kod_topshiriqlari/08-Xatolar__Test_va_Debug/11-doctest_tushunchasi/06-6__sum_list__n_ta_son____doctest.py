import doctest

def sum_list(lst):
    """
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([5])
    5
    >>> sum_list([])
    0
    """
    return sum(lst)

if __name__ == "__main__":
    doctest.testmod()
    
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
        
    print(sum_list(numbers))