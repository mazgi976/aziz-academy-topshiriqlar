import doctest

def add(a, b):
    """
    >>> add(1, 2)
    3
    >>> add(5, 7)
    12
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod()
    
    a, b = map(int, input().split())
    print(add(a, b))