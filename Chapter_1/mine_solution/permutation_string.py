import unittest


def is_permutation(string1, string2):

    if len(string1) != len(string2):
        return False

    count_dict = {}

    for char in string1:
        if count_dict.get(char):
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    for char in string2:
        if count_dict.get(char) == None:
            return False
        elif count_dict.get(char) < 1:
            return False
        else:
            count_dict[char] -= 1
    return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_is_permutation(self):
        # true check
        for test_strings in self.dataT:
            result = is_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = is_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
