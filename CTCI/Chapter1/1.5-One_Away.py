# CTCI 1.5
# One Away

import unittest
from collections import Counter

# My Solution
# Have a counter for each character and check if it is one off in three cases
# Iterates through a set to only get unique characters
def one_away(str1, str2):
    one = False
    counter1 = Counter()
    counter2 = Counter()
    length1 = len(str1)
    length2 = len(str2)

    if str1 == str2:
        return True

    for c in str1:
        counter1[c] += 1
    for c in str2:
        counter2[c] += 1

    # Check for add
    if length2 > length1:
        for c in set(str2):
            if counter1[c] < counter2[c]:
                if one:
                    return False
                one = True
            elif counter1[c] > counter2[c]:
                return False
    # Check for remove
    elif length2 < length1:
        for c in set(str1):
            if counter1[c] < counter2[c]:
                return False
            elif counter1[c] > counter2[c]:
                if one:
                    return False
                one = True
    # Check for replace
    else:
        for c in set(str2):
            if counter1[c] < counter2[c]:
                if one:
                    return False
                one = True
    return True

#-------------------------------------------------------------------------------
# CTCI Solution

def one_away2(s1, s2):
    '''Check if a string can converted to another string with a single edit'''
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

#-------------------------------------------------------------------------------
#Testing

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
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
