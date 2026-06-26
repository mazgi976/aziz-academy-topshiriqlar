import unittest

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        
    def test_safe_div(self):
        self.assertEqual(safe_div(10, 2), 5.0)
        self.assertRaises(ZeroDivisionError, safe_div, 10, 0)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOperations)
    unittest.TextTestRunner().run(suite)
    
    try:
        op = input()
        if op == "ADD":
            x = int(input())
            y = int(input())
            print(add(x, y))
        elif op == "EVEN":
            x = int(input())
            print("EVEN" if is_even(x) else "ODD")
        elif op == "DIV":
            x = int(input())
            y = int(input())
            try:
                print(f"{safe_div(x, y):.2f}")
            except ZeroDivisionError:
                print("DIV0")
    except (ValueError, EOFError):
        pass