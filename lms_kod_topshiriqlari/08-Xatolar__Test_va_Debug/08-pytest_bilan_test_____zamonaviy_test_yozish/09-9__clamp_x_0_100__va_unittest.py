import unittest

def clamp(x):
    if x < 0:
        return 0
    elif x > 100:
        return 100
    return x

class TestClamp(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(-1), 0)
        self.assertEqual(clamp(101), 100)
        self.assertEqual(clamp(50), 50)
        
if __name__ == '__main__':
    x = int(input())
    print(clamp(x))
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)