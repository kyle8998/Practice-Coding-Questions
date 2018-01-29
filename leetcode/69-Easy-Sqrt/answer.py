#!/usr/bin/env python

#-------------------------------------------------------------------------------
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
#-------------------------------------------------------------------------------
# Testing
