import doctest

def max_of_two(a, b):
    """
    >>> max_of_two(1, 2)
    2
    """
    return a if a > b else b

if __name__ == "__main__":
    doctest.testmod()
    
    a, b = map(int, input().split())
    print(max_of_two(a, b))