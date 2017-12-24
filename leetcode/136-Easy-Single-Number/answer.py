#!/usr/bin/env python

#-------------------------------------------------------------------------------
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use xor bit manipulation to find the unique number
        result = 0
        for n in nums:
            result ^= n
                
        return result
#-------------------------------------------------------------------------------
# Testing
