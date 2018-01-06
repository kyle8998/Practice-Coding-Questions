#!/usr/bin/python

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = ""
        for i in range(len(s)):
            # Takes in account odd and even cases
            result = max(result, self.find_palindrome(s, i, i), self.find_palindrome(s, i, i+1), key=len)        
            
        return result
            
    # Helper method to find the longest palindrome starting from the center
    def find_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

#-------------------------------------------------------------------------------
#Testing
