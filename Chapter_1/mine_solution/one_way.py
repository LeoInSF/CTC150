import unittest

def is_one_way(str1, str2):

    length_str1 = len(str1)
    lenght_str2 = len(str2)
    intersection_list = [x for x in list(str1) if x in list(str2)]
    print intersection_list
    # zero edit
    if length_str1 - lenght_str2 == 0 and len(intersection_list) == length_str1:
        return True

    # replace
    if length_str1 - lenght_str2 == 0 and len(intersection_list) == length_str1 - 1:
        return True
    # remove
    if length_str1 - lenght_str2 == 1 and len(intersection_list) in [length_str1 - 1, length_str1]:
        return True

    # insert
    if length_str1 - lenght_str2 == -1 and len(intersection_list) == length_str1:
        return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_one_way(test_s1, test_s2)
            print test_s1, test_s2
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
