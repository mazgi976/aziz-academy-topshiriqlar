import doctest

def clamp(x):
    """
    >>> clamp(-1)
    0
    >>> clamp(150)
    100
    >>> clamp(50)
    50
    """
    if x < 0:
        return 0
    if x > 100:
        return 100
    return x

if __name__ == "__main__":
    doctest.testmod()
    
    x = int(input())
    print(clamp(x))