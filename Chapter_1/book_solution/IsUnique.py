import unittest

def unique(string):

    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for char in string:
        val = ord(char)
        if char_set[val]:
            # duplicate char
            return False

        char_set[val] = True

    return True

class Test(unittest.TestCase):
    test_data_1 = [('abcd'), ('s4fad'), ('')]
    test_data_2 = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true test
        for test_str in self.test_data_1:
            actual = unique(test_str)
            self.assertTrue(actual)

        # test false
        for test_str in self.test_data_2:
            actual = unique(test_str)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()

# complexity O(n)
