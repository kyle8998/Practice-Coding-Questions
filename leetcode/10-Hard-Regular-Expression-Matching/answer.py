#!/usr/bin/python

#------------------------------------------------------------------------------
# My cheaty one liner
# re.match matches a regular expression to a string. The first parameter is the pattern,
# the second is the string, and the third is any special rules used. I concatenate '^'
# and '$' to the pattern because those signify the start and ending of the line. I then
# use re.M as the rule because it enforces the ^ and $ match for the line. It returns
# the match object on sucess and None on failure, I can just convert this to a boolean
# because we only want a true/false value.
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