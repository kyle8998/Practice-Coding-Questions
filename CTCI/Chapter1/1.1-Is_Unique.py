# CTCI 1.1
# Is Unique

import unittest

# My Solution
def isUnique(string):
    list = []

    for c in string:
        if c not in list:
            list.append(c)
        else:
            return False
    return True

#-------------------------------------------------------------------------------
# CTCI Solution
def isUnique2(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

#-------------------------------------------------------------------------------
#Testing

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
