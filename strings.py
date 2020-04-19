#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    return find_index(text, pattern, False) != None

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    #loop through text checking if a letter in the text is the pattern first letter
    if pattern == "": #all strings contain the empty string pattern
        return 0

    text_index = 0
    pattern_index = 0
    while text_index != len(text):
        print("Text Index",text_index)
        print("Pattern Index", pattern_index)
        text_letter = text[text_index]
        pattern_letter = pattern[pattern_index] #have a match
        if text_letter == pattern_letter:
            print("Have a match", text_letter)
            if pattern_index == len(pattern) -1: #end of pattern
                return text_index -len(pattern) +1 #fix this later to first index found
            else: #not at end yet
                pattern_index += 1
                text_index += 1
        else: #not a match
            pattern_index = 0
            if text_letter != pattern[0]:
                text_index += 1
       

def find_all_indexes(text, pattern, flag = False):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODOplement find_all_indexes here (iteratively and/or recursively)
    i = 1
    j = 1
    l=list()
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            if flag == True:
                l.append(i)
                return l
            else:
                l.append(i)
    return l

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    print(find_index("abc", ""))
    print(find_all_indexes('abc',''))
