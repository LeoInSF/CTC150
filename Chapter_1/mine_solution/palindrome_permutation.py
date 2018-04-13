from collections import Counter
import unittest

def is_palindrome_permutation(string):

    new_str = string.lower().replace(' ', '')

    if (sum(freq % 2 for char, freq in Counter(new_str).items()) < 2):
        return True

    else:
        return False


class TestPalindromePermutation(unittest.TestCase):

    def test_is_palindrome_permutation(self):

        test_dataT = ['Tact Coa', 'abc cba', 'aba']
        test_dataF = ['abcd', 'aabcd', 'bbb aaa ccd']

        for test_string in test_dataT:
            self.assertTrue(is_palindrome_permutation(test_string))

        for test_string in test_dataF:
            self.assertFalse(is_palindrome_permutation(test_string))

if __name__ == '__main__':
    unittest.main()
