import unittest

def is_palindrome(s):
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('abba'))
        self.assertFalse(is_palindrome('abc'))
        
if __name__ == '__main__':
    s = input()
    if is_palindrome(s):
        print("YES")
    else:
        print("NO")
        
    unittest.main(argv=['first-arg-is-ignored'], exit=False)