#!/usr/bin/python

#------------------------------------------------------------------------------
# DP Solution
#------------------------------------------------------------------------------

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # 2D Cache to store the results
        # Each row is a char of the pattern
        # Each col is a char of the string
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Each star can eliminate the * char if there are no occurances
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # For the pattern:
                    # If the pattern is a *, it will be true if:
                    # Case 1: The previous char matched (1+ occurances of * char)
                    # Case 2: The char before the previous matched (0 occurances of * char)
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # For the string:
                    # Case 1: * char is equal to the current string char
                    # Case 2: the * char is a . so accept everything
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] = table[i][j] or table[i][j - 1]

        return table[-1][-1]
        
#------------------------------------------------------------------------------
# My cheaty one liner
# re.match matches a regular expression to a string. The first parameter is the pattern,
# the second is the string, and the third is any special rules used. I concatenate '^'
# and '$' to the pattern because those signify the start and ending of the line. I then
# use re.M as the rule because it enforces the ^ and $ match for the line. It returns
# the match object on sucess and None on failure, I can just convert this to a boolean
# because we only want a true/false value.
#------------------------------------------------------------------------------

import re

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # Simple RegEx match enforcing the match to be the entire line
        return bool(re.match('^'+p+'$', s, re.M))

#------------------------------------------------------------------------------
#Testing