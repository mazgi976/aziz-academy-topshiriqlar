import doctest

def factorial(n):
    """
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    doctest.testmod()
    
    n = int(input())
    print(factorial(n))