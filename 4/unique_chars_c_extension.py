import unique_chars

def check_unique_chars(s):
    return unique_chars.has_unique_chars(s)

if __name__ == "__main__":
    test_string = "abcdef"
    print(f"Does '{test_string}' have all unique characters? {check_unique_chars(test_string)}")
    test_string = "hello"
    print(f"Does '{test_string}' have all unique characters? {check_unique_chars(test_string)}")
