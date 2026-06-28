import doctest

def add(a, b):
    """
    >>> add(5, 3)
    8
    >>> add(-1, 1)
    0
   """
    return a + b

def is_palindrome(s):
    """
    >>> is_palindrome('anna')
    True
    >>> is_palindrome('hello')
    False
    """""
    return s == s[::-1]

def clamp(x):
    """
    >>> clamp(50)
    50
    >>> clamp(150)
    100
    """
    if x < 0:
        return 0
    elif x > 100:
        return 100
    return x

if __name__ == "__main__":
    doctest.testmod()
    
    op = input().strip()
    
    if op == 'ADD':
        x = int(input())
        y = int(input())
        print(add(x, y))
        
    elif op == 'PAL':
        s = input().strip()
        print("YES" if is_palindrome(s) else "NO")
        
    elif op == 'CLAMP':
        x = int(input())
        print(clamp(x))