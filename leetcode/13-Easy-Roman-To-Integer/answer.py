#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            if s[i] =='M':
                result += 1000
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'C':
                if (i+1) < len(s) and (s[i+1] == 'D' or s[i+1] == 'M'):
                    result -= 100
                else:
                    result += 100
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'X':
                if (i+1) < len(s) and (s[i+1] == 'C' or s[i+1] == 'L'):
                    result -= 10
                else:
                    result += 10
            elif s[i] == 'V':
                result += 5
            elif s[i] == "I":
                if (i+1) < len(s) and (s[i+1] == 'X' or s[i+1] == 'V'):
                    result -= 1
                else:
                    result += 1
        
        return result

#------------------------------------------------------------------------------
#Testing

