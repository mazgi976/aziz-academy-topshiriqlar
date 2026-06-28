import doctest

def reverse_str(s):
    """
    >>> reverse_str('abc')
    'cba'
    """""
    return s[::-1]

if __name__ == "__main__":
    doctest.testmod()
    
    s = input()
    print(reverse_str(s))