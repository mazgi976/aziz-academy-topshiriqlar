import unittest

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

class TestVowelCount(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_vowels('hello'), 2)
        self.assertEqual(count_vowels('python'), 1)
        
if __name__ == '__main__':
    s = input()
    print(count_vowels(s))
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)