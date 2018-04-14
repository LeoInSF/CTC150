import unittest

def string_compression(string):
    tmp_str = ''
    pre_char = ''
    char_count = 0

    for char in string:
        if pre_char == '':
            pre_char = char
            char_count += 1
            continue

        elif pre_char == char:
            char_count += 1
            continue

        else:
            tmp_str += pre_char + str(char_count)
            pre_char = char
            char_count = 1

    tmp_str += pre_char + str(char_count)

    if len(tmp_str) < len(string):
        return tmp_str
    else:
        return string
'''
https://waymoot.org/home/python_string/
Method 6: List comprehensions is the fastest way to do string concatenation
'''

class Test(unittest.TestCase):

    def test_string_compression(self):
        test_data = [('aabcccccaaa', 'a2b1c5a3'),
                        ('aabbccdd', 'aabbccdd')]

        for [input, expected] in test_data:
            self.assertEqual(string_compression(input), expected)

if __name__ == '__main__':
    unittest.main()
