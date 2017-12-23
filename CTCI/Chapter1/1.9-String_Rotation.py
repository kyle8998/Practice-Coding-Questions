# CTCI 1.9
# String Rotation

import unittest

# Is Substring Function
def is_substring(string, sub):
    return string.find(sub) != -1

# My Solution

def string_rotation(s1, s2):
    if len(s1) == len(s2):
        return is_substring(s2+s2, s1)
    return False

#-------------------------------------------------------------------------------
# CTCI Solution
# Had the same solution
#-------------------------------------------------------------------------------
#Testing

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
