import unittest

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
        
class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(7, 5), 1)
        
if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGCD)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
    try:
        a, b = map(int, input().split())
        print(gcd(a, b))
    except (ValueError, EOFError):
        pass