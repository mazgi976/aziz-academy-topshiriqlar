import unittest

def reverse_str(s):
    return s[::-1]

class TestReverseStr(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str('abc'), 'cba')
        self.assertEqual(reverse_str('python'), 'nohtyp')
        
if __name__ == '__main__':
    s = input()
    print(reverse_str(s))
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)