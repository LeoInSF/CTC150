import unittest

# incorrect solution!!!
def isSubString(s1, s2):

    char_dict1 = {}
    char_dict2 = {}

    for char in s1:
        if char_dict1.get(char):
            char_dict1[char] += 1
        else:
            char_dict1[char] = 1

    for char in s2:
        if char_dict2.get(char):
            char_dict2[char] += 1
        else:
            char_dict2[char] = 1
    print char_dict1, char_dict2
    for k,v in char_dict1.items():
        if v == char_dict2.get(k):
            continue
        else:
            return False

    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ('aaabbbccc', 'bcaacbbca', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = isSubString(s1, s2)
            print s1, s2
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
