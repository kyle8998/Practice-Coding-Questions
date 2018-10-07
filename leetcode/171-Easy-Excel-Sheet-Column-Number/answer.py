#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, result = 0, 0
        for letter in s[::-1]:
            digit = (ord(letter)-ord('A'))+1
            for _ in range(i):
                digit *= 26
            i += 1
            result += digit
        return result
        
#-------------------------------------------------------------------------------
