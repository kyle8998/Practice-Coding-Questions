#!/usr/bin/env python3

#-------------------------------------------------------------------------------
import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W*', '', s).lower()
        return s == s[::-1]
#-------------------------------------------------------------------------------
