#!/usr/bin/env python

#-------------------------------------------------------------------------------
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0
        for i in range(length):
            if s[i] == ' ':
                # If there are consecutive spaces at the end!
                space = True
                while space:
                    if i+1 < length:
                        if s[i+1] == ' ':
                            i += 1
                        else:
                            count = 0
                            space = False
                    else:
                        space = False
            else:
                count += 1
                
        return count
#-------------------------------------------------------------------------------
# Testing
