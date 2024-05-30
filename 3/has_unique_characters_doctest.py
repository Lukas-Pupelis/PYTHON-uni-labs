
# This script defines a function to check for unique characters in a string using doctests.

def has_unique_characters(s):
    """
    Determine if the string `s` consists of all unique characters.
    
    >>> has_unique_characters("abcde")
    True
    >>> has_unique_characters("hello")
    False
    >>> has_unique_characters("")
    True
    """
    return len(set(s)) == len(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
