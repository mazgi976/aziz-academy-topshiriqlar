import unittest

def parse_int(s):
    return int(s)

class TestParseInt(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(parse_int("10"), 10)
        self.assertRaises(ValueError, parse_int, "abc")
        
if __name__ == '__main__':
    s = input()
    try:
        print(parse_int(s))
    except ValueError:
        print("BAD")
        
    unittest.main(argv=['first-arg-is-ignored'], exit=False)