import unittest

def urlify(string, length):
    str_length = len(string)

    for i in range(length-1, -1, -1):

        if string[i] == ' ':
            string[str_length - 3: str_length] = '%20'
            str_length -= 3

        else:
            string[str_length - 1] = string[i]
            str_length -= 1
    return string


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
