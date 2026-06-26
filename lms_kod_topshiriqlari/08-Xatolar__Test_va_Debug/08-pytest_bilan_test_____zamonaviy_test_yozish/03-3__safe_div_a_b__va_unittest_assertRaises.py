import unittest

def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

class TestSafeDiv(unittest.TestCase):
    def test_safe_div(self):
        self.assertRaises(ZeroDivisionError, safe_div, 10, 0)
        self.assertEqual(safe_div(10, 2), 5.0)
        
if __name__ == '__main__':
    try:
        a, b = map(int, input().split())
        print(f"{safe_div(a, b):.2f}")
    except ZeroDivisionError:
        print("DIV0")
        
    unittest.main(argv=['first-arg-is-ignored'], exit=False)