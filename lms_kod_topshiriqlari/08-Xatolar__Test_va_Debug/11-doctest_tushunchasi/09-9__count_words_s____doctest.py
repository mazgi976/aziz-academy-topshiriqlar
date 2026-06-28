import doctest

def count_words(s):
    """
    >>> count_words('a b c')
    3
    >>> count_words('Salom dunyo')
    2
    >>> count_words('')
    0
    """
    return len(s.split())

if __name__ == "__main__":
    doctest.testmod()
    
    s = input()
    print(count_words(s))