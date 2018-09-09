#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# O(n) solution

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.addDigits(sum(int(i) for i in str(num))) if num>=10 else num


#-------------------------------------------------------------------------------
# O(1) Solution

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
#-------------------------------------------------------------------------------
