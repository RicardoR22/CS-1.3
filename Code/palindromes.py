#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):

    # Set left index to 0, set right index to the last index of the given text
    left = 0
    right = len(text) - 1

    while left < right:
        # Set left_char the character at the left index in text, Set right_char the character at the right index in text
        left_char = text[left]
        right_char = text[right]

        # Check if left_char is an alphabet character
        if not left_char.isalpha():
            # If it's not, we don't care for it so we increase left index by 1
            left += 1
            # continue on to the next iteration of the loop
            continue

        # Check if right_char is an alphabet character
        if not right_char.isalpha():
            # If it's not, we don't care for it so we increase right index by 1
            right -= 1
            # continue on to the next iteration of the loop
            continue

        # Compare the two letters to see if they are the same
        if left_char.lower() == right_char.lower():
            # If they are the same, increase/decrease the indexes
            left += 1
            right -= 1
            continue
        else:
            # If they're not, return false since this text is not a palindrome
            return False

    return True



def is_palindrome_recursive(text, left=None, right=None):
    # Set left index to 0, set right index to the last index of the given text
    if left is None:
        left = 0
        right = len(text) - 1

    if left >= right:
        return True

    # Set left_char the character at the left index in text, Set right_char the character at the right index in text
    left_char = text[left]
    right_char = text[right]

    # Check if left_char is an alphabet character
    if not left_char.isalpha():
        # If it's not, we don't care for it so we increase left index by 1
        left += 1
        return is_palindrome_recursive(text, left, right)

    # Check if right_char is an alphabet character
    if not right_char.isalpha():
        # If it's not, we don't care for it so we increase right index by 1
        right -= 1
        return is_palindrome_recursive(text, left, right)

    # Compare the two letters to see if they are the same
    if left_char.lower() == right_char.lower():
        # If they are the same, increase/decrease the indexes
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)
    else:
        # If they're not, return false since this text is not a palindrome
        return False




def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
