
# This script defines unittests for the function that checks if a string has unique characters.

def has_unique_characters(s):
    return len(set(s)) == len(s)

import unittest

class TestHasUniqueCharacters(unittest.TestCase):
    def test_unique_characters(self):
        self.assertTrue(has_unique_characters("abcde"))

    def test_non_unique_characters(self):
        self.assertFalse(has_unique_characters("hello"))
        
    def test_empty_string(self):
        self.assertTrue(has_unique_characters(""))

if __name__ == '__main__':
    unittest.main()
