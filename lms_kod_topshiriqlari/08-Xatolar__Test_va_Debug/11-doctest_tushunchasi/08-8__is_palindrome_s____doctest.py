import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abc')
    False
    """""
    return s == s[::-1]

if __name__ == "__main__":
    doctest.testmod()
    
    s = input()
    if is_palindrome(s):
        print("YES")
    else:
        print("NO")