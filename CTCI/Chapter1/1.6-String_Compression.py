# CTCI 1.6
# String Compression

import unittest

# My Solution
def string_compression(string):
    count = 1
    result = []
    
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            result.append(string[i-1] + str(count))
            count = 0
        count += 1
    result.append(string[i] + str(count))

    return min(string, ''.join(result), key=len)


#-------------------------------------------------------------------------------
# CTCI Solution


#-------------------------------------------------------------------------------
#Testing

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
