import unittest

def uniq_count(lst):
    return len(set(lst))

class TestUniqCount(unittest.TestCase):
    def test_uniq(self):
        self.assertEqual(uniq_count([1, 1, 2]), 2)
        self.assertEqual(uniq_count([1, 2, 3, 4]), 4)
        self.assertEqual(uniq_count([5, 5, 5, 5]), 1)
        
if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUniqCount)
    unittest.TextTestRunner().run(suite)
    
    try:
        n = int(input())
        lst = [int(input()) for _ in range(n)]
        print(uniq_count(lst))
    except (ValueError, EOFError):
        pass