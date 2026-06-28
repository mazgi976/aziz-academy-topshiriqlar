import doctest

def avg(lst):
    """
    >>> avg([1, 2, 3])
    2.0
    >>> avg([])
    0.0
    """
    if not lst:
        return 0.0
    return sum(lst) / len(lst)

if __name__ == "__main__":
    doctest.testmod()
    
    try:
        n = int(input())
        numbers = []
        for _ in range(n):
            numbers.append(int(input()))
            
        result = avg(numbers)
        print(f"{result:.2f}")
    except (ValueError, EOFError):
        print("0.00")