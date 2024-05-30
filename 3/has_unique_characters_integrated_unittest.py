
# This script integrates doctests into unittests for the function checking if a string has unique characters.

import unittest
import doctest
import has_unique_characters_doctest  # Assuming the doctest file is named like this and is accessible

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(has_unique_characters_doctest))
    return tests

if __name__ == '__main__':
    unittest.main()
