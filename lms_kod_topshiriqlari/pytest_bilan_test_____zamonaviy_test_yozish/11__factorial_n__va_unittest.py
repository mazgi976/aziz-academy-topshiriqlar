import unittest

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        
if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)