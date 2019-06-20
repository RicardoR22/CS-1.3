#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Time Complexity: O(n) because of the find_all_indexes function
    Space Complexity: O(n) because of the find_all_indexes function"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    found_indexes = find_all_indexes(text, pattern) # O(n) time and space

    if found_indexes == []: # O(1) time
        return False # O(1) time

    return True # O(1) time



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Time Complexity: O(n) because of the find_all_indexes function
    Space Complexity: O(n) because of the find_all_indexes function"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    found_indexes = find_all_indexes(text, pattern) # O(n) time and space

    if found_indexes == []: # O(1) time
        return None # O(1) time

    return found_indexes[0] # O(1) time


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time Complexity: O(n) where n is the number of characters between index 0 and our max_index
    Space Complexity: O(n) where n is the number of items in the array holding our indexes"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) is not 0: # O(1) time
        max_index = len(text) - (len(pattern) - 1) # O(1) time, O(1) space
    else:
        max_index = len(text) # O(1) time

    indexes = [] # O(1) time, O(n) since we don't know how many items will go into the array

    for index in range(0, max_index): # O(n) time where n is the number of characters between 0 and max_index
        curr_range = index + len(pattern) # O(1) time, O(1) space
        curr_letters = text[index:curr_range] # O(1) space

        if curr_letters == pattern: # O(1) time
            indexes.append(index) # O(1) time

    return indexes # O(1) time


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
    main()
