#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# O(1) Bit Manipulation
#-------------------------------------------------------------------------------

class Solution(object):
    def isPowerOfTwo(self, n):
        # Explanation
        # We know the powers of two have one set single bit in binary
        # We also know then a perfect square-1 would have all of the bits ahead set
        # n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.
        # If we AND them, the result should be 0 if a perfect square
        return n > 0 and not (n & (n-1))

#-------------------------------------------------------------------------------
# O(1) Bit Count
#-------------------------------------------------------------------------------
        
class Solution(object):
    def isPowerOfTwo(self, n):
        # Explanation
        # We know perfect squares of 2 only have 1 set bit in binary
        return n > 0 and bin(n).count("1") == 1
        
#-------------------------------------------------------------------------------
# O(log(n)) Division
#-------------------------------------------------------------------------------

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

#-------------------------------------------------------------------------------