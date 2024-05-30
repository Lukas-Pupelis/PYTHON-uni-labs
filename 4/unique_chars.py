def has_unique_chars(s):
    return len(s) == len(set(s))

if __name__ == "__main__":
    test_string = "abcdef"
    print(f"Does '{test_string}' have all unique characters? {has_unique_chars(test_string)}")
    test_string = "hello"
    print(f"Does '{test_string}' have all unique characters? {has_unique_chars(test_string)}")
