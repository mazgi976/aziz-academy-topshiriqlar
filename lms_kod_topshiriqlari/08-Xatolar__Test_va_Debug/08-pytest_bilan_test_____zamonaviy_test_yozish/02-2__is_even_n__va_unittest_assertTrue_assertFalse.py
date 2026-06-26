import unittest

def is_even(n):
    return n % 2 == 0

class TestEvenFunction(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        
if __name__ == '__main__':
    n = int(input())
    
    if is_even(n):
        print("EVEN")
    else:
        print("ODD")
        
    unittest.main(argv=['first-arg-is-ignored'], exit=False)