#!/usr/bin/env python

#-------------------------------------------------------------------------------

class Solution(object):
    def isPalindrome(self, x):

        temp = x
        digits = 1
        # If x is negative
        if x < 0:
            return False

        # Find 1^digits
        while temp >= 10:
            temp /= 10
            digits *= 10

        # While there are numbers left
        while x:
            if ((x % 10) != (x / digits)):
                return False
            # Removes a digit off each side
            x = x % digits / 10
            # Removes 2 digits
            digits /= 100;

        return True

#-------------------------------------------------------------------------------
#Testing

def main():
    x = Solution()
    y = x.isPalindrome(1234321)
    print y

main()
