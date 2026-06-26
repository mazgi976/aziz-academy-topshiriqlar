import unittest

def max_of_two(a, b):
    return a if a > b else b

class TestMaxFunction(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_of_two(5, 10), 10)
        self.assertEqual(max_of_two(-1, -5), -1)
        
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(max_of_two(a, b))
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)