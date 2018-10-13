#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Bit Manipulation Solution
#-------------------------------------------------------------------------------

class Solution:
    def findTheDifference(self, s, t):
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

#-------------------------------------------------------------------------------
# Dict Solution
#-------------------------------------------------------------------------------
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
                
        for c in t:
            if c in chars and chars[c] > 0:
                chars[c] -= 1
            else:
                return c
        return None
#-------------------------------------------------------------------------------
