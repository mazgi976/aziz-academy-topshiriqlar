import doctest

def is_even(n):
    """
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """""
    return n % 2 == 0

if __name__ == "__main__":
    doctest.testmod()
    
    n = int(input())
    if is_even(n):
        print("EVEN")
    else:
        print("ODD")