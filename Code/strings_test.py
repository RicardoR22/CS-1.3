#!python

from strings import contains, find_index, find_all_indexes, contains_recursive
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        assert contains('racecar', 'ace') is True
        assert contains('yellow', 'ello') is True
        assert contains('cocacola', 'ola') is True

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        assert contains('orange', 'orn') is False
        assert contains('chocolate', 'let') is False
        assert contains('light', 'igt') is False

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert contains('melloyello', 'ello') is True
        assert contains('amumu', 'mu') is True
        assert contains('assessment', 'ess') is True

    def test_contains_recursive_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains_recursive('abc', '') is True  # all strings contain empty string
        assert contains_recursive('abc', 'a') is True  # single letters are easy
        assert contains_recursive('abc', 'b') is True
        assert contains_recursive('abc', 'c') is True
        assert contains_recursive('abc', 'ab') is True  # multiple letters are harder
        assert contains_recursive('abc', 'bc') is True
        assert contains_recursive('abc', 'abc') is True  # all strings contain themselves
        assert contains_recursive('aaa', 'a') is True  # multiple occurrences
        assert contains_recursive('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        assert contains_recursive('racecar', 'ace') is True
        assert contains_recursive('yellow', 'ello') is True
        assert contains_recursive('cocacola', 'ola') is True


    def test_contains_recursive_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains_recursive('abc', 'z') is False  # remember to test other letters
        assert contains_recursive('abc', 'ac') is False  # important to test close cases
        assert contains_recursive('abc', 'az') is False  # first letter, but not last
        assert contains_recursive('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        assert contains_recursive('orange', 'orn') is False
        assert contains_recursive('chocolate', 'let') is False
        assert contains_recursive('light', 'igt') is False

    def test_contains_recursive_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains_recursive('ababc', 'ab') is True  # multiple occurrences
        assert contains_recursive('banana', 'na') is True  # multiple occurrences
        assert contains_recursive('ababc', 'abc') is True  # overlapping prefix
        assert contains_recursive('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert contains_recursive('melloyello', 'ello') is True
        assert contains_recursive('amumu', 'mu') is True
        assert contains_recursive('assessment', 'ess') is True

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        # TODO: Write more positive test cases with assert equal int statements
        assert find_index('bottle', 'tle') == 3
        assert find_index('league', 'agu') == 2

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        assert find_index('orange', 'orn') is None
        assert find_index('chocolate', 'let') is None
        assert find_index('light', 'igt') is None

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert find_index('melloyello', 'ello') == 1
        assert find_index('amumu', 'mu') == 1
        assert find_index('assessment', 'ess') == 3

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
        # TODO: Write more positive test cases with assert equal list statements
        assert find_all_indexes('racecar', 'ace') == [1]
        assert find_all_indexes('yellow', 'ello') == [1]
        assert find_all_indexes('cocacola', 'co') == [0, 4]

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        assert find_all_indexes('orange', 'orn') == []
        assert find_all_indexes('chocolate', 'let') == []
        assert find_all_indexes('light', 'igt') == []

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert find_all_indexes('melloyello', 'ello') == [1, 6]
        assert find_all_indexes('amumu', 'mu') == [1, 3]
        assert find_all_indexes('assessment', 'ss') == [1, 4]


if __name__ == '__main__':
    unittest.main()
