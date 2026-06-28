import doctest

def parse_int(s):
    """
    >>> parse_int('10')
    10
    >>> parse_int('abc')
    'BAD'
     """
    try:
        return int(s)
    except ValueError:
        return 'BAD'
    
if __name__ == "__main__":
    doctest.testmod()
    
    s = input()
    print(parse_int(s))