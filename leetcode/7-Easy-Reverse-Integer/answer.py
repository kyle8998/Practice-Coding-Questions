#!/usr/bin/env python

#-------------------------------------------------------------------------------

class Solution(object):
        def reverse(self, x):
            """
            :type x: int
            :rtype: int
            """

            # Create integer and boolean
            reverse = 0
            neg = False
            # If x is negative, trigger a boolean and remove negative
            if x < 0:
                neg = True
                x *= -1

            # Loop through each digit
            while x != 0:
                # Calculate reverse per digit
                reverse = (reverse * 10) + (x % 10)
                # Divide x by 10 to get to next digit
                x /= 10

            # Hardcoded max for 32 bit signed integer
            # Probably not optimal
            if reverse > 0x7FFFFFFF:
                return 0

            # Readd the negative sign if applicable
            if neg:
                return -reverse
            return reverse

#-------------------------------------------------------------------------------
#Testing

def main():
    x = Solution()
    y = x.reverse(-123)
    print y
    y = x.reverse(10)
    print y
    # Should overflow
    y=x.reverse(8463847412)
    print y

main()
