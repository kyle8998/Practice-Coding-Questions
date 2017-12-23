# CTCI 1.2
# Check Permutation

import unittest
from collections import Counter

# My Solution
def palindrome_permutation(string):
    one = False

    if len(string) % 2 == 0:
        even = True
    else:
        even = False

    counter = Counter()
    # Increment counter for each chat
    for c in string:
        counter[c] += 1

    for c in string:
        if counter[c] % 2 != 0:
            if one or even:
                return False
            one = True

    return True



#-------------------------------------------------------------------------------
# CTCI Solution
def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1

def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1

#-------------------------------------------------------------------------------
#Testing

class Test(unittest.TestCase):
    '''Test Cases'''
    ''' I disagree with these palindromes '''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            print(actual)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
