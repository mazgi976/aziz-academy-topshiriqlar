import unittest

def sum_list(lst):
    return sum(lst)

class TestSumList(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
        self.assertEqual(sum_list([10, -10, 5]), 5)
        
if __name__ == '__main__':
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    
    print(sum_list(lst))
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)