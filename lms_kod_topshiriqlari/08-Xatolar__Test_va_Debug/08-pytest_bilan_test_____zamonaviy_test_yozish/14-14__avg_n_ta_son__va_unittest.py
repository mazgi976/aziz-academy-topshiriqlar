import unittest

def avg(lst):
    if not lst:
        return 0.0
    return sum(lst) / len(lst)

class TestAvg(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(avg([1, 2, 3]), 2.0)
        self.assertEqual(avg([]), 0.0)
        self.assertEqual(avg([10, 20]), 15.0)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAvg)
    unittest.TextTestRunner().run(suite)
    
    try:
        n_input = input()
        if n_input:
            n = int(n_input)
            lst = [int(input()) for _ in range(n)]
            print(f"{avg(lst):.2f}")
    except (ValueError, EOFError):
        pass